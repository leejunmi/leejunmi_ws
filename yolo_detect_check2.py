# 1458 수정
import torch
from ultralytics import YOLO
import cv2
import numpy as np


class YoloDetect:
    def __init__(self):
        self.pt = '/home/leejunmi/Downloads/jeju_lane.pt' 
        # self.video_path = '/home/leejunmi/Downloads/_talkv_ww3VhXXJyG_2sI4qFwXSQEitjE9DC8Dik_talkv_high.MP4'    
        self.video_path = '/home/leejunmi/Downloads/short_ver.MP4'
        self.model = YOLO(self.pt)
        self.left_xy = None
        self.right_xy = None
        self.frame_width = 640
        self.frame_height = 360
        self.result_image = None

    def video_detect(self):
        video = cv2.VideoCapture(self.video_path)

        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                print('!!!! video 종료 !!!!')
                break  # 비디오 끝나면 루프 종료

            new_frame = frame.copy()
            self.result_image = frame.copy()

            roi_h = self.frame_height / 2

            # self.result_image = self.result_image[int(roi_h):,:]
            results = self.model(frame,conf=0.5)  # YOLO 모델로 객체 탐지 실행

            # results가 비어있는지 확인
            print(f"results: {results}")

            self.find_lane(new_frame, results)

            cv2.imshow('result', self.result_image)

            if cv2.waitKey(1) == ord('q'):
                break


        video.release()
        cv2.destroyAllWindows()  # 모든 윈도우 종료
        
    def find_leftright(self, mask): 
        # print(mask_x)
        mask = np.array(mask)
        mask_x = mask[:,0]

        x_mean = np.mean(mask_x)
        # print(x_mean)

        if x_mean < self.frame_width / 2:
            self.left_xy = mask
        else:
            self.right_xy = mask

    def find_lane(self, new_frame, results):

        if not results:  
            print("No results found.")
            return 

        for result in results:

            print(f"Detected objects: {result.names}") 
            print(f"Number of masks: {len(result.masks.xy) if result.masks else 0}")  # 마스크 개수

            if result.masks:  
                masks = result.masks.xy 
                # masks = np.array(masks)
                print(f"Number of masks: {len(masks)}")  # 마스크 개수 : 이상적인건 2
                
                if len(masks) == 2:
                    for mask in masks:
                        self.find_leftright(mask) 

                # 양쪽 차선이 있을 때와 한쪽만 있을 때 마스크를 모두 처리
                if self.left_xy is not None:
                    print('                                                                                                  왼쪽 차선 존재함')
                    self.create_xy(self.left_xy, (0, 255, 255))  # Yellow for left lane

                if self.right_xy is not None:
                    print('                                                                                                  오른쪽 차선 존재함')
                    self.create_xy(self.right_xy, (255, 0, 0))  # Blue for right lane
  
            else:
                print('no mask')

    def create_xy(self, points, color):

        points = np.array(points)
        new_xy = []
        

        x_data = points[:,0]
        y_data = points[:,1]

        for x,y in points:
            cv2.circle(self.result_image, (int(x), int(y)), 3, color, -1)

def main():
    yolodetect = YoloDetect()
    yolodetect.video_detect()

if __name__ == "__main__":
    main()
