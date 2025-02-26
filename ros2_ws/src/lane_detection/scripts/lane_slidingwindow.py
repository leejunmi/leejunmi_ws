import cv2
import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures
# import matplotlib.pyplot as plt
# from std_msgs.msg import Int8

def histogram(warp_img):

    histogram = np.sum(warp_img[int(warp_img.shape[0]/2):, :], axis=0) 
    mid_point = np.int16(warp_img.shape[0]/2)

    start_leftX = np.argmax(histogram[:320]) if np.any(histogram[:320] > 0) else -1 # 히스토그램 왼쪽 최대 구하기(시작점)
    start_rightX = np.argmax(histogram[320:]) + 320 if np.any(histogram[320:] > 0) else 641 # 히스토그램 오른쪽 최대 구하기(시작점)

    # left_max_value = histogram[:320].max()q
    # right_max_value = histogram[320:].max() 
    # print(f'detect: left:{start_leftX} right:{start_rightX}')

    # left 값들 처리
    if (start_leftX > 300) and pre_leftx: # 300으로 변경
        # print(f'left 값 넘어감 current left:{start_leftX}, pre_left:{pre_leftx[-1]}')
        current_leftX = pre_leftx[-1] 
    # 왼 차선 안 보이는 경우
    elif start_leftX == -1 and len(pre_leftx) > 1 and len(pre_rightx) > 1:
        pre_distance = abs(pre_rightx[-1] - pre_leftx[-1]) 
        # print('왼쪽 안 보임')
        current_leftX = start_leftX - pre_distance*0.05
    # left_x값 튈 경우
    elif len(pre_leftx) > 1 and (abs(pre_leftx[-1] - start_leftX) >= 60) and (pre_leftx[-1] > 0): # 지난 x가 안 보이는 경우였으면 뺵 
        # print(f'left/ current left:{start_leftX}, pre_left:{pre_leftx[-1]}') 
        current_leftX = pre_leftx[-1] 

    else: 
        current_leftX = start_leftX


    # right 값들 처리
    if (start_rightX < 340) and pre_rightx: # 340으로 변경
        # print('start right 범위 넘어감')
        current_rightX = pre_rightx[-1] # 
    # 오른 차선 안 보일 경우
    elif start_rightX == 641 and len(pre_leftx) > 1 and len(pre_rightx) > 1: # histogram 안 들어오면 641
        pre_distance = abs(pre_rightx[-1] - pre_leftx[-1]) 
        # print('오른쪽 안 보임')
        current_rightX = start_rightX + pre_distance*0.05
        # current_rightX = start_rightX

    # right_x값 튈 경우
    elif len(pre_rightx) > 1 and (pre_rightx and (abs(pre_rightx[-1] - start_rightX) >= 60)) and (pre_rightx[-1] < 640):
        # print(f'right/ current right:{start_rightX}, pre_right:{pre_rightx[-1]}') 
        current_rightX = pre_rightx[-1] 
    else:
        current_rightX = start_rightX

    pre_leftx.append(current_leftX) 
    pre_rightx.append(current_rightX) 

    mean_center = sliding_window(current_leftX, current_rightX)
    
def sliding_window(current_leftX, current_rightX):
    num_windows = 12 # 윈도우 개수
    window_h = np.int16(warp_img.shape[0] / num_windows) 
    nonzero = warp_img.nonzero()
    nonzeroy = np.array(nonzero[0])
    nonzerox = np.array(nonzero[1])

    min_num_pixel = 30
    window_margin = 40 # 윈도우 

    win_left_lane = []
    win_right_lane = []

    center_points = []


    for window in range(num_windows):
        window_y_low = warp_img.shape[0] - (window + 1) * window_h 
        window_y_high = warp_img.shape[0] - window * window_h
        window_leftx_min = current_leftX - window_margin
        window_leftx_max = current_leftX + window_margin
        window_rightx_min = current_rightX - window_margin
        window_rightx_max = current_rightX + window_margin

        current_centerX = int((current_rightX + current_leftX) / 2)
        current_centerY = int((window_y_high + window_y_low) / 2)

        center_pts = np.float32([[current_centerX, current_centerY]]).reshape(-1,1,2)
        real_center = cv2.perspectiveTransform(center_pts, Minv).reshape(-1,2).astype(int)


        if window == 2 or window == 4 or window == 6  : # 11,9,7
            center_points.append((tuple(real_center[0])))
            cv2.circle(result_img, tuple(real_center[0]), 3, (255,0,0), -1) 
            cv2.circle(real_img, tuple(real_center[0]), 3, (255,0,0), -1)
        
        if window == 11:
            first_center = real_center[0][0]
            # print(f'f: {first_center}')
        if window == 7:
            last_center = real_center[0][0]
        
    
        cv2.rectangle(warp_img, (int(window_leftx_min), int(window_y_low)),(int(window_leftx_max), int(window_y_high)), (255,255,0),2)
        cv2.rectangle(warp_img, (int(window_rightx_min), int(window_y_low)),(int(window_rightx_max), int(window_y_high)), (255,255,0),2)
        cv2.circle(warp_img, (current_centerX, current_centerY), 2, (255,255,255), -1)
        # print(f'center point: {real_center}')
        # line_regression(real_center)

        left_window_inds = ((nonzeroy > window_y_low) & (nonzeroy < window_y_high) & (nonzerox > window_leftx_min) & (nonzerox < window_leftx_max)).nonzero()[0]
        right_window_inds = ((nonzeroy > window_y_low) & (nonzeroy < window_y_high) & (nonzerox > window_rightx_min) & (nonzerox < window_rightx_max)).nonzero()[0]

        win_left_lane.append(left_window_inds) # 현재 윈도우에서 검출된 픽셀 수 저장
        win_right_lane.append(right_window_inds)

        if len(right_window_inds) > min_num_pixel:
            current_rightX = np.int16(np.mean(nonzerox[right_window_inds]))

        if len(left_window_inds) > min_num_pixel: 
            current_leftX = np.int16(np.mean(nonzerox[left_window_inds]))

    # left, right lane을 fillpoly로 그리기

    # win_left_lane = np.concatenate(win_left_lane)
    # win_right_lane = np.concatenate(win_right_lane)

    # leftx, lefty = nonzerox[win_left_lane], nonzeroy[win_left_lane]
    # rightx, righty = nonzerox[win_right_lane], nonzeroy[win_right_lane]
    # print(f'l:{leftx}, r:{rightx}')

    # pts_left = np.array([list(zip(leftx, lefty))], dtype=np.int32)
    # pts_right = np.array([list(zip(rightx, righty))], dtype=np.int32)

    # cv2.fillPoly(warp_img, [pts_left], (255, 255, 255)) 
    # cv2.fillPoly(warp_img, [pts_right], (255, 255, 255))

    # steer 계산
    center_points = np.array(center_points)
    mean_center = np.mean(center_points[:,0])

    steerr = (mean_center-320)/64  # -5~5 사이의 값으로 
    # print(steerr)

    diff = first_center - last_center # diff가 + 이면 우회전, -이면 좌회전
    print(f'steer: {steerr}, diff: {diff}')


    a = 5
    if abs(diff) > 1:
        steerr = steerr + diff/a # parameter 조정
        # 스티어가 생각보다 많이 돌아간다면 a 늘리기

    steerr = np.clip(steerr,-5.5, 5.5)   

    # steer는 전체 -22~22, 12로 나눈 값으로 들어감

    if steerr >= 5.5:
        steer = 'right6'
    elif steerr >= 4.5:
        steer = 'right5'
    elif steerr >= 3.5:
        steer = 'right4'
    elif steerr >= 2.5:
        steer = 'right3'
    elif steerr >= 1.5:
        steer = 'right2'
    elif steerr >= 0.5:
        steer = 'right1'
    elif steerr >= 0:
        steer = 'right0'
    
    elif steerr <= -5.5:
        steer = 'left6'
    elif steerr <= -4.5:
        steer = 'left5'
    elif steerr <= -3.5:
        steer = 'left4'
    elif steerr <= -2.5:
        steer = 'left3'
    elif steerr <= -1.5:
        steer = 'left2'
    elif steerr <= -0.5:
        steer = 'left1'
    elif steerr < 0:
        steer = 'left0'
    # else: 
    #     steer = 'straight'
    
    rounded_steer = round(steerr, 1) # 얘를 퍼블리시 하기

    cv2.putText(real_img, steer, (20,20), cv2.FONT_HERSHEY_TRIPLEX, 0.7, (0,100, 200), 1, cv2.LINE_AA)
    cv2.putText(real_img, str(rounded_steer), (20,45), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,100, 200), 1, cv2.LINE_AA)


    return rounded_steer # -5.5 ~ 5.5의 값 



# def line_regression(points):
#     if len(points) == 0:
#         print("No center points detected for regression.")
#         return  # 데이터가 없으면 회귀 중단
#     center_points = np.array(points)

#     real_x = center_points[:, 0]
#     real_y = center_points[:, 1]
#     center_real = np.reshape(real_x, (-1, 1))

#     poly_features = PolynomialFeatures(degree=1) 
#     x_train_poly = poly_features.fit_transform(center_real)

#     linear_reg = LinearRegression()
#     linear_reg.fit(x_train_poly, real_y)

#     X_new = np.arange(100,500).reshape(-1, 1)
#     X_new = np.linspace(min(real_x), max(real_x), 50).reshape(-1, 1)


#     X_new_poly = poly_features.fit_transform(X_new)
#     y_new = linear_reg.predict(X_new_poly)
    

#     for x,y in zip(X_new, y_new):
#         cv2.circle(real_img, (int(x),int(y)), 1, (255,255,255), -1)  


video_path = '/home/leejunmi/Downloads/_talkv_ww3VhXXJyG_2sI4qFwXSQEitjE9DC8Dik_talkv_high.MP4'
# video_path = '/home/leejunmi/Downloads/8min (1).mp4'

video = cv2.VideoCapture(video_path)

pre_leftx = []
pre_rightx = []

while video.isOpened():
    ret, img = video.read()
    current_leftX = None
    current_rightX = None

    # 좌우반전 버전으로 할 시 다음 줄 주석 제거
    img = cv2.flip(img,1)

    real_img = cv2.resize(img, (640,360))
    img = cv2.cvtColor(real_img, cv2.COLOR_BGR2GRAY) 

    img = cv2.GaussianBlur(img, (7,7), 0)
    img = cv2.Canny(img, 100,250)

    h = img.shape[0]
    w = img.shape[1]

    src = np.float32([[80,h/4], 
                [560,h/4], # 원래 80, 560
                [0,h-180],
                [w,h-180]]) # parameter 조정 필요함
    
    dst = np.float32([[0,0],
                    [w,0],
                    [0,h],
                    [w,h]])

    M = cv2.getPerspectiveTransform(src, dst)
    Minv = cv2.getPerspectiveTransform(dst, src) # warp한 이미지를 다시 바꾸기 위한 행렬 
    warp_img = cv2.warpPerspective(img, M, (640,360))

    result_img = cv2.warpPerspective(warp_img, Minv, (640,360))

    cv2.line(real_img, (0,real_img.shape[0]//2), (real_img.shape[1],real_img.shape[0]//2), (255,255,255), 1, cv2.LINE_AA)
    cv2.line(real_img, (real_img.shape[1]//2, 0), (real_img.shape[1]//2, real_img.shape[0]), (255,255,255), 1, cv2.LINE_AA) # 중간에 라인 생성

    histogram(warp_img)

    warp_img_colored = cv2.cvtColor(warp_img, cv2.COLOR_GRAY2BGR)  # stack 하기 위함
    combined_img = np.hstack((warp_img_colored, real_img))

    cv2.imshow('result', combined_img)
    if cv2.waitKey(20) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()


# 각도 변경시 조절해야하는 값
# 1. warp 파라미터
# 2. 튈 때 예외처리하는 값

# 8min 영상으로 재생했을 때, 레인 여러 개 보이는 구간에서 튀었음 -> 근데 그냥 최대 steer로 유지됨.. 어떤 문제가 생기는 지는 더 알아보기