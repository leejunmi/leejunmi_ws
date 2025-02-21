import numpy as np
import open3d as o3d 
from sklearn.linear_model import RANSACRegressor, LinearRegression
# rclpy
import rclpy
from rclpy.node import Node
import rclpy.time
import rclpy.timer
# msg
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import Header
from sensor_msgs.msg import PointCloud2
import sensor_msgs_py.point_cloud2 as pc2
from geometry_msgs.msg import Point


class Lidar_Lane(Node):
    def __init__(self):
        super().__init__('lidar_lane')
        self.sub = self.create_subscription(PointCloud2, '/points', self.pointcloud_callback, 10)

        self.publisher = self.create_publisher(MarkerArray, 'lane_marker', 10)
        # self.publisher_line = self.create_publisher(Marker, 'line', 10)

        self.timer = self.create_timer(0.1, self.visualization_and_publish) 

        self.lane_points = None

        self.lane_line = None
    
    def pointcloud_callback(self, msg):
        ''' 
        callback 함수
        포인트 받아서 intensity 80 이상인 점들만 받아서 self.points에 저장
        args: msg, PointCloud2 형식
        '''
        try:
            self.points = [] 
            for point in list(pc2.read_points(msg, field_names=('x','y','z','intensity'), skip_nans=True)):
                if point[3] > 70: # intensity 조건 
                    self.points.append([point[0], point[1], point[2]]) 

            self.points = np.array(self.points, dtype='float32')   
      
            if self.points.size == 0: # numpy: len보다 size가 적합!! 
                self.get_logger().info('no points')

            self.left_lane_points = self.points[(self.points[:,2] < 0.1) & (self.points[:,1] < -1)] # numpy 벡터 연산
            self.right_lane_points = self.points[(self.points[:,2] < 0.1) & (self.points[:,1] > 1)] # y기준 왼오 나눔

        except Exception as e:
            print(f'{e}')
            self.get_logger().info(f'Failed in callback,{e}')
           

    def ransac_reg(self, lane_points): 
        '''
        ransac regression을 진행, inliear에 해당하는 점들만 추출
        args
        : lidar_data: numpy.ndarray
        return
        : self.lane_points(regression 후 points, /geometry_msgs/Point 형식)
        
        '''
        if lane_points.size > 0:

            X = lane_points[:,0].reshape(-1, 1) # 2차원 배열
            y = lane_points[:,1] # 1차원 배열

            # RANSAC 회귀 실행
            ransac = RANSACRegressor()
            ransac.fit(X, y)

            # train_y = ransac.predict(X) # 삭제

            inlier_mask = ransac.inlier_mask_

            new_x = np.arange(-15,15).reshape(-1,1)
            new_y = ransac.predict(new_x)
            
            self.lane_points = [Point(x=float(p[0]),y=float(p[1]),z=0.0) for p in zip(X[inlier_mask].flatten(), y[inlier_mask])] 
            # X는 2차원 배열, 1차원으로 flatten 필요
            # z도 float으로 넣어주기

            self.lane_line = [Point(x=float(p[0]), y=float(p[1]), z=0.0) for p in zip(new_x, new_y)]

            return self.lane_points, self.lane_line


    def visualization_and_publish(self): 
        '''
        회귀 후의 점들, 선을 marker로 visualization하기 위해 MarkerArray publish하는 함수
  
        create_marker에서 얻은 Marker 리스트를 MarkerArray로 만듦
        '''
        self.ransac_pcd =[]

        try:
            self.ransac_pcd, left_lane_pcd = self.ransac_reg(self.left_lane_points) 
            right_ransac_pcd, right_lane_pcd = self.ransac_reg(self.right_lane_points)
            
            self.ransac_pcd.extend(right_ransac_pcd)

            header = Header() 
            header.stamp = self.get_clock().now().to_msg() 
            header.frame_id = 'lidar'

            marker_array = MarkerArray()
            marker_array.markers.extend(self.create_markers(self.ransac_pcd, 'lane', 0, Marker.POINTS, 0.2, 0.2, 0.0, 1.0, 1.0)) 
            marker_array.markers.extend(self.create_markers(left_lane_pcd, 'left', 1, Marker.LINE_STRIP, 0.1, 0.1, 1.0, 1.0, 1.0))
            marker_array.markers.extend(self.create_markers(right_lane_pcd, 'right',2, Marker.LINE_STRIP, 0.1, 0.1, 1.0, 1.0, 1.0))

            self.publisher.publish(marker_array)

        except Exception as e:
            self.get_logger().info(f'failed in visualization_and_publish,{e}')



    def create_markers(self, points, ns, id, type, x,y,r,g,b): 
        '''
        marker 생성하는 함수 
        args: points(geometry.msgs/Point), ns, id, type(marker), 그외 scale,color
        return: marker
        '''
        markers = []

        marker = Marker()
        marker.header.frame_id = 'lidar'
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = ns 
        marker.id = id
        marker.type = type 
        marker.action = Marker.ADD
        marker.scale.x = x
        marker.scale.y = y
        marker.color.r = r
        marker.color.g = g
        marker.color.b = b
        marker.color.a = 1.0

        try:
            # points
            marker.points = points 
            markers.append(marker)
            self.get_logger().info('success marker points')
            
        except Exception as e:
            self.get_logger().info(f'failed marker points: {e}')

        return markers


def main(args=None):
    rclpy.init(args=args)
    lidar_Lane = Lidar_Lane()
    try:
        rclpy.spin(lidar_Lane) 
    except Exception as e:
        print(f'error : {e}')
    finally:
        rclpy.shutdown()

if __name__=='__main__':
    main()
    
    ros2 단일스레드, 스핀 하나 돌리면 스레드 하나 차지.
    두 파일을 사용하거나 한 파일로 멀티스레드... 
