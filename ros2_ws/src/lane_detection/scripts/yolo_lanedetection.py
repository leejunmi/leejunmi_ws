#!/usr/bin/env python3


import torch
from ultralytics import YOLO
import cv2
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from scipy.interpolate import CubicSpline # 안 씀
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class YoloDetect(Node):
    def __init__(self):
        super().__init__('lane_steer')
        self.publisher = self.create_publisher(String, '/lane_steer_direction', 10)
        self.pt = '/home/leejunmi/ros2_ws/src/lane_detection/scripts/lane1000.pt' 
        self.video_path = '/home/leejunmi/ros2_ws/src/lane_detection/scripts/jeju_lane_video.MP4'

        self.model = YOLO(self.pt)
        
        self.left_xy = None
        self.right_xy = None
        self.frame_width = 640 # result_image.shape[1]
        self.frame_height = 360 # result_image.shape[0]
        self.result_image = None
        self.center_points = []

        self.left_line = []
        self.right_line = [] # 직선 

        self.pre_left_m = None
        self.pre_right_m = None 

        self.pre_center_m = None

        self.pre_left = None
        self.pre_right = None

        self.direction = None

    def video_detect(self):
        video = cv2.VideoCapture(self.video_path)

        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                print('#### video 종료 ####')
                break  # 비디오 끝나면 루프 종료

            # 이미지 좌우 반전
            frame = cv2.flip(frame,1)

            new_frame = frame.copy()
            self.result_image = frame.copy()

            roi_h = self.frame_height / 2

            # self.result_image = self.result_image[int(roi_h):,:]
            results = self.model(frame,conf=0.5)

            self.find_lane(new_frame, results)

            cv2.line(self.result_image, (0,self.result_image.shape[0]//2), (self.result_image.shape[1],self.result_image.shape[0]//2), (255,255,255), 1, cv2.LINE_AA)
            cv2.line(self.result_image, (self.result_image.shape[1]//2, 0), (self.result_image.shape[1]//2, self.result_image.shape[0]), (255,255,255), 1, cv2.LINE_AA) # 중간에 라인 생성

            cv2.imshow('result', self.result_image)

            if cv2.waitKey(2) == ord('q'):
                break


        video.release()
        cv2.destroyAllWindows()  

    def find_lane(self, new_frame, results):

        if not results:  
            print("No results found.")
            return 

        for result in results:

            if result.masks:  
                masks = result.masks.xy 
                # masks = np.array(masks)
                print(f"Number of masks: {len(masks)}")  # 마스크 개수 : 이상적인건 2
                
                if len(masks) > 0:
                    if len(masks) == 3:
                        print('################### mask 3개 ###################') 
                    
                    for mask in masks:
                         # 왼 오 레인 구분, self.에 저장
                        self.find_leftright(mask)
                        
                    if np.array(self.left_xy).any() and np.array(self.right_xy).any():

                        # y 하나당 x값 한 개만 가지도록 수정
                        self.left_xy = self.create_xy(self.left_xy)
                        self.right_xy = self.create_xy(self.right_xy) 

                        # 왼오 포인트에 대해 1차회귀
                        reg_left_points = self.lane_regression(self.left_xy,(0,255,255),1) 
                        reg_right_points = self.lane_regression(self.right_xy, (255,0,0),1) 

                        # 회귀 line에 해당하는 직선 추출 
                        left_line_x, left_line_y, left_x, left_m, left_b = self.find_mb(reg_left_points,0,(0,255,255)) 
                        right_line_x, right_line_y, right_x, right_m, right_b = self.find_mb(reg_right_points,1,(255,255,0)) # x는 y=0일때의 x값

                        # 최종 직선을 가지고 겹치는지 판단하여 레인 그리기
                        left, right = self.create_lane(left_line_x, left_line_y,right_line_x, right_line_y,left_x, left_m, left_b, right_x, right_m, right_b)

                        # 직선 기반 center 생성 및 그리기
                        reg_center_points = self.make_center(left, right) 
                        # center line의 정보 찾기
                        line_x, line_y,center_x, center_m, center_b = self.find_mb(reg_center_points,2,(255,0,255))

                        self.calculate_direction(center_m, reg_center_points)

                    else:
                        print(' #### no lane ####')
            else:
                print('no mask')


    def find_leftright(self, mask): 
        ''' 각 마스크의 평균값으로 왼오 lane 판단'''

        mask = np.array(mask)
        mask_x = mask[:,0] 
        mask_y = mask[:,1]
        for_mean_x = mask_x[mask_y > self.frame_height / 3] # 2/3만 left, right 판단에 사용

        if for_mean_x.size > 1:
            x_mean = np.mean(for_mean_x)
        elif for_mean_x.size == 1:
            x_mean = for_mean_x
        else:
            print('find_leftright error: no points') 
            x_mean = np.mean(mask_x)

        # roi 설정 -> 하니까 더 안 됨 ㅡㅜㅜ
        if (x_mean < self.frame_width / 2):
            mask = mask[(mask_x <= 320)] #& (mask[:,1] > self.frame_height/5)] # 하단 4/5만 보기

            if mask.shape[0] > 30:
                self.left_xy = np.array(mask)
            else:
                print('### 이전 값 사용, 픽셀 값 안 넘음')

        else:
            mask = mask[(mask_x > 320)] #& (mask[:,1] > self.frame_height/5)] 
            self.right_xy = np.array(mask)


    def create_xy(self, points):
        '''y값 하나당 x값 한 개(평균값)만 가지도록 하는 함수'''

        points = np.array(points)
        new_xy = []

        if points.size == 0:
            print('create_xy error: no points')
            return new_xy
        
        x_data = points[:,0]
        y_data = points[:,1]

        y_data = np.unique(y_data)

        for aim_y in y_data: # y값에 대해 반복
            x_for_calculate = []
            for x,y in points: # 각 point에 대해 반복
                if int(y) == int(aim_y):
                    x_for_calculate.append(x)
            
            if len(x_for_calculate) > 1:
                new_x = np.mean(x_for_calculate)
            elif len(x_for_calculate) == 1:
                new_x = x_for_calculate[0]
            # print(int(aim_y),x_for_calculate)
            new_xy.append((int(new_x), int(aim_y)))  
        
        if len(new_xy) == 0:
            print('create_xy: no new_xy')
            new_xy = points

        return new_xy



    def make_center(self, left, right): 
        '''y가 같은 점을 찾아 중간점을 검출하기, regression한 self.center_points 리턴
         self.center_points 안 들어오는 부분 있는지 확인  '''
        
        left = np.array(left) 
        right = np.array(right) # 크기는 30,30 , 전체 점을 30개로 나눴으니 y교집합은 당연히 똑같지...
       
        common_y = np.intersect1d(left[:,1].astype(int), right[:,1].astype(int)) # 교집합 찾기
        # print(f'common_y: {common_y}') 

        if len(common_y) > 0: # common_y는 30개
            self.center_points = []
            for y in common_y:
                # left_x = left[(int(y)-10 < left[:,1]) & (left[:,1] < int(y)+10)][:,0] # 동일 y값에 해당하는 x 찾기 -> 범위 늘림.
                # right_x = right[(int(y)-10 < right[:,1]) & (right[:,1] < int(y)+10)][:,0]
                left_x = left[left[:,1] == y][:,0]
                right_x = right[right[:,1] == y][:,0]

                if len(left_x) > 1:
                    mean_left_x = np.mean(left_x)
                elif len(left_x) == 1:
                    mean_left_x = left_x
                
                if len(right_x) > 1:
                    mean_right_x = np.mean(right_x)
                elif len(right_x) == 1:
                    mean_right_x = right_x

                self.center_points.append(( ((float(mean_left_x) + float(mean_right_x))/2) , y))  # 혹은 item

        elif len(self.center_points)==0: 
            # 처음부터 센터포인트 없을때:  프레임 중앙으로 center point 형성하기 -> 왜 안되는 건지 모르겠음
            # steer 주는 경우에는, 그냥 steer=0(직진)으로 주는 게 나을듯
            print('no common y')
            center_x = np.ones(30)*(self.result_image.shape[1]/2)
            center_y = np.linspace(0, self.result_image.shape[0], 30)
            self.center_points = np.column_stack((center_x, center_y)) # 열별 쌓기
        else:
            # 이전 self는 있고 common_y는 없을 때 -> self 업데이트 안 함(이전값 사용)
            print('common_y 없음, 이전 값 사용') 
            
    
        center_points = self.center_points

        if np.any(center_points):
            for x,y in center_points:
                cv2.circle(self.result_image, (int(x),int(y)), 3, (0,0,0), -1) # 여기서 센터 출력
                # 최대y쪽 값이 튐. 왜이러냐????
        else:
            print('regression center points 없음!!')

        return np.array(center_points)


    def find_mb(self, reg_line, num, color):
        '''regression된 lane에서 1차함수m,b, 함수 기반 점들을 추출하는 함수
            b 필요없음? -> 수정 해야해'''
    
    
        reg_line_x = reg_line[:,0] # !!! center에 대해서 추출 안 될 때 예외처리 필요함 -> 일단햇음
        reg_line_y = reg_line[:,1]

        min_x, max_x = np.argmin(reg_line_x), np.argmax(reg_line_x)
        x1, x2 = np.min(reg_line_x), np.max(reg_line_x) 
        y1, y2 = reg_line_y[min_x], reg_line_y[max_x]

        Red = (0,0,255)
        m, b = self.cal_ab(x1,y1,x2,y2)

        # m값 제한
        if abs(m)<0.5:
            print(' ')
            print('@@@@@@ m 범위 벗어남 @@@@@@@')
            print(' ')
            m = float('inf') 

        if num == 0: # left line    
            print(f'left lane 기울기는 {m}')
        if num == 1:
            print(f'right lane 기울기는 {m}')
        if num ==2:
            print(f'center 기울기는 {m}')

        # y=mx+b, y=0일때 x값은 -b/m
        # 근데 카메라 좌표계, y=-mx+b 이면 b/m
        # m=0일때 처리해야함
        x = b/m

        # 그린 직선의 (x,y) 30개 찾기 -> 각 끝 점의 x,y를 구한다
        if x1==x2 or np.isnan(m):
                x = x1
                m = 100
                b = 0

        # 직선 찾기
        # y=mx+b라 하면 맨 아래 점은 y=self.frame_height x:(self.frame_height-b)/m, y:self.frame_height
        # 맨 위에 점은 y=0, x:-b/m

        line_x = np.linspace((self.frame_height-b)/m, -b/m, 30)
        line_y = np.linspace(self.frame_height, 0, 30)

        return line_x, line_y, x, m, b

    def cal_ab(self,x1,y1,x2,y2):
        '''두 점으로 기울기와 y절편을 구함'''

        # y = ax + b

        try:
            a = (y2 - y1)/(x2 - x1)
            b = (x2*y1 - x1*y2)/(x2 - x1)
        except:
        # if x2==x1 or np.isnan(a) or np.isnan(b):
            a = 100 
            b = 0
            
        return a,b

    def create_lane(self,left_line_x, left_line_y,right_line_x, right_line_y, left_x, left_m, left_b, right_x, right_m, right_b):
        '''왼오 레인 직선 겹치면 이전 값 유지(self 값 이용), 결과 왼오 라인 리턴
        args
            left_x: left lane의 y=0일때의 x값(top_x)
            right_x: right lane의 y=0일때의 x값(top_x -> 겹치는지에 대한 판단을 위함
            left_line_x, left_line_y: 회귀+직선으로 만든 left line
            right_line_x, right_line_y: 회귀+직선으로 만든 right line -> 값 업데이트 시 사용
        Returns
            result_left_line: 최종 left 직선
            result_right_line: 최종 right 직선
            '''
         

        if right_x > left_x: # 왼오 라인 침범하면
            print(' ')
            print(' ==== 이전 값 사용 ===')
            print('  ')
    
            result_left_line = []
            result_right_line = []

            for x, y in self.pre_left:  
                cv2.circle(self.result_image, (int(x),int(y)), 3, (0,255,255), -1)
                result_left_line.append((x,y))

            for x,y in self.pre_right:
                result_right_line.append((x,y))
                cv2.circle(self.result_image, (int(x),int(y)), 3, (255,255,0), -1)

        else: # 정상적인 경우 -> line 값 업데이트해서 self에서 처리하기
            self.left_line = []
            self.right_line = []

            # 수정
            result_left_line = []
            result_right_line = []
            for x,y in zip(left_line_x, left_line_y):
                cv2.circle(self.result_image, (int(x),int(y)), 3, (0,255,255), -1)
                result_left_line.append((x,y))

            for x,y in zip(right_line_x,right_line_y):
                cv2.circle(self.result_image, (int(x),int(y)), 3, (255,255,0), -1)
                result_right_line.append((x,y))

            # self.pre_left_m, self.pre_right_m = left_m, right_m 

            # 추가
            self.pre_left = result_left_line
            self.pre_right = result_right_line

        return result_left_line, result_right_line

    def lane_regression(self, points, color, degree):
        '''regression 하는 함수
        1차 회귀만 할 거면 Polynomial 안 써도 될듯.
        self.center_points 받아서 regression한 numpy point 생성'''


        result_points = []
        if len(points) == 0: # 근데 이 경우가 있으면 안 됨 ...
            print("No center points detected for regression.")
            return  # 데이터가 없으면 회귀 중단
        points = np.array(points, dtype=np.float32)

        real_x = points[:, 0]
        real_y = points[:, 1]
        real_x = np.reshape(real_x, (-1, 1))

        poly_features = PolynomialFeatures(degree = degree) # polynomial 객체 생성
        x_train_poly = poly_features.fit_transform(real_x) # 객체로 train_poly 생성 -> 이때 인풋(-1,1)

        linear_reg = LinearRegression() # LinearRegression 객체 생성
        linear_reg.fit(x_train_poly, real_y) # polynomial로 생성한 x_train_poly로 linear_reg 피팅

        X_new = np.linspace(min(real_x), max(real_x), 30).reshape(-1, 1)

        X_new_poly = poly_features.fit_transform(X_new) # linear_reg에 넣기 위한 fitting
        y_new = linear_reg.predict(X_new_poly)
        
        result_points = np.column_stack((X_new.flatten(), y_new.flatten())) # dimension error 나서 ...

        return np.array(result_points)
    
    def calculate_direction(self,x, center_lane):
        '''center 점을 받아서 가장 작은 y(=0)값의 x를 기준으로 right/left/straight를 판단하는 함수
        Args
            center_lane: 회귀 후 직선으로 만든 center points, NDArray ? 
        Returns
            self.direction: 어느 방향으로 꺾어야 하는지 판단'''
        
        center_x = self.frame_width/2
        top_center_x = center_lane[:,0][0] 
      
        print(f'top: {top_center_x}') # y=360일때 값 이상함. ㅠㅠㅠ 

        
        # if center_x - 40 < top_center_x < center_x + 40: # 640중 80
        #     self.direction = 'straight'
        # elif top_center_x <= center_x - 40: # 40
        #     self.direction = 'left1'
        # else: 
        #     self.direction = 'right' # 40

        if center_x - 30 < top_center_x < center_x + 30: 
            self.direction = 'straight'
        elif top_center_x <= center_x - 80: 
            self.direction = 'left2'
        elif top_center_x <= center_x - 30:
            self.direction = 'left1'
        elif top_center_x > center_x + 80: 
            self.direction = 'right2'
        elif top_center_x > center_x + 30:
            self.direction = 'right1'
        else:
            self.direction = 'straight'

        msg = String() # std_msgs.msg.String 타입의 메세지 객체
        msg.data = self.direction

        self.publisher.publish(msg) # ''형식으로 직접 퍼블리시할 수 없음, 메세지 객체만 퍼블리시 가능함
    
        cv2.putText(self.result_image, self.direction,(20,20), cv2.FONT_HERSHEY_TRIPLEX, 0.8, (0,100, 200), 1, cv2.LINE_AA)
        
    # ===============================================

    def draw_lane(self, lane: np.ndarray, color):
        '''lane 채워서 출력'''
        lane = np.int_([lane]) # filPoly 에서는 2D 배열 int형식의 리스트 필요로 함 

        cv2.fillPoly(self.result_image, lane, color)


    
def main(args=None):
    rclpy.init(args=args)
    yolodetect = YoloDetect()
    yolodetect.video_detect()

    try:
        rclpy.spin('lane_steer')
    except Exception as e:
        print(f'error: {e}')
    finally:
        rclpy.shutdown()

if __name__ == "__main__":
    main()

