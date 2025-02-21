import numpy as np
import open3d as o3d # 사실 안 씀(no noise에서 )
import rclpy
from rclpy.node import Node
import rclpy.time
import rclpy.timer
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import Header
from sensor_msgs.msg import PointCloud2
import sensor_msgs_py.point_cloud2 as pc2
from geometry_msgs.msg import Point
# Point /Point32 ?? 
import numpy as np


class Lidar_Lane(Node):
    def __init__(self):
        super().__init__('lidar_lane')
        self.sub = self.create_subscription(PointCloud2, '/points', self.pointcloud_callback, 10)

        self.publisher = self.create_publisher(MarkerArray, 'lane_marker', 10)

        self.timer = self.create_timer(0.1, self.visualization_and_publish) # 0.1초마다 visualization_and_publish 실행
    
    def pointcloud_callback(self, msg):
        ''' 
        callback 함수
        포인트 받아서 intensity 90 이상인 점들만 받아서 self.points에 저장
        args: msg(PointCloud2)
        '''
        try:
            self.points = [] # 콜백 들어올 때마다 self.points 초기화
            for point in pc2.read_points(msg, field_names=('x','y','z','intensity'), skip_nans=True):
                if point[3] > 90:
                    #self.points.append(Point(point[0],point[1],point[2]))
                    self.points.append(Point(x=float(point[0]), y=float(point[1]), z=float(point[2])))
                    # self.points 리스트에는 Point 형식 xyz값 포함 
                    # Point에는 위치인수로 저장X, 값 지정해주기
                #self.get_logger().info(f'points: {self.points}')
            if len(self.points) == 0:
                self.get_logger().info('no points')
        except Exception as e:
            print(f'{e}')
            self.get_logger().info(f'Failed in callback,{e}')
        


    def visualization_and_publish(self): 
        '''
        self.points 점들을 marker로 visualization하기 위해 MarkerArray publish하는 함수
        create_marker에서 얻은 Marker 리스트를 MarkerArray로 만듦
        '''
        try:
            # self.get_logger().info('visualization and publish')
            header = Header() 
            header.stamp = self.get_clock().now().to_msg() # stamp는 왜 필요
            header.frame_id = 'lidar' # 임의로 해도 되는거?

            marker_array = MarkerArray()
            marker_array.markers.extend(self.create_markers(self.points)) 
            # 근데 여러 points가 있잖아!! 
            self.publisher.publish(marker_array)
            #self.get_logger().info('퍼블리시') 

        except Exception as e:
            self.get_logger().info(f'failed in visualization_and_publish,{e}')


    def create_markers(self, lane_points):
        '''
        marker 생성하는 함수 
        '''
        markers = []

        try:
            marker = Marker()
            marker.header.frame_id = 'lidar'
            marker.header.stamp = self.get_clock().now().to_msg() # 왜 필요?
            marker.ns = 'lane'
            marker.id = 0
            marker.type = Marker.POINTS
            marker.action = Marker.ADD
            marker.scale.x = 0.2
            marker.scale.y = 0.2
            marker.color.r = 0.0
            marker.color.g = 1.0
            marker.color.b = 1.0
            marker.color.a = 1.0
            
            try:
                #marker.points = [Point(x=p.x, y=p.y, z=p.z) for p in lane_points] 
                # 위치인수로 지정해줄 수 없음. 
                marker.points = lane_points
                markers.append(marker)
                self.get_logger().info('success marker points')
            except Exception as e:
                self.get_logger().info(f'failed marker points: {e}')


        except Exception as e:
            pass
            #self.get_logger().info(f'Failed in create_markers, {e}') # marker 생성 실패

        return markers


def main(args=None):
    rclpy.init(args=args) # rclpy 시작
 
    lidar_Lane = Lidar_Lane() # 인스턴스 생성 

    try:
 
        rclpy.spin(lidar_Lane) # 콜백 실행
    except Exception as e:
        print(f'error : {e}')
    finally:
        rclpy.shutdown()

    # init으로 초기화 -> 인스턴스 생성 -> spin으로 callback 호출 -> shutdown
     
if __name__=='__main__':
    main()
