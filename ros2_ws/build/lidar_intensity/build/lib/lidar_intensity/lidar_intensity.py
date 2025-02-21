import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
import sensor_msgs_py.point_cloud2 as pc2
# 메서드 사용하기 위한(read_points나 create_cloud) 임포트
import numpy as np

class ContinuousBagToNumpy(Node):
    def __init__(self):
        '''
        init
        sub 받기
        all_points 리스트 생성
        '''
        super().__init__('continuous_bag_to_numpy')

        self.subscription = self.create_subscription(PointCloud2, '/points', self.pointcloud_callback, 10)
        self.all_points = []

    def pointcloud_callback(self, msg):
        '''
        콜백함수
        read_points로 포인트 받아서 all_points 리스트에 각각 저장 
        '''
        try:
            for point in pc2.read_points(msg, field_names=('x', 'y', 'z', 'intensity'), skip_nans=True):
                # field_names=() 소괄호 써야함
                # skip_nans는 nan이 포함된 배열을 스킵할지 여부
                # 출력은 필드 데이터를 튜플로 반환함 
                self.all_points.append((point[0], point[1], point[2], point[3]))
                # point를 각각 따로 담지 않으면 numpy array로 변환+float32로 바꿀때 오류 
                # 수정: [point[0], ,,, ]-> () 소괄호로

            # self.save_data()
            self.get_logger().info(f"Collected {len(self.all_points)} points so far.")
        except Exception as e:
            self.get_logger().error(f"Error processing point cloud: {e}")

    def save_data(self):
        '''
        all_points를 array로 바꾸고 np.save로 저장 
        '''
        try:
            self.get_logger().info('save_data 실행됨')
            structured_dtype = np.dtype([('x', 'f4'), ('y', 'f4'), ('z', 'f4'), ('intensity', 'f4')])

            all_points_array = np.array(self.all_points, dtype=structured_dtype)
            filename = 'collected_pointclouds_noise_수정.npy'
            np.save(filename, all_points_array)
            self.get_logger().info(f"Saved collected data to {filename}")
        except Exception as e:
            self.get_logger().error(f"Error saving data: {e}")


def main(args=None):
    rclpy.init(args=args) #노드 초기화
    node = ContinuousBagToNumpy() #클래스 인스턴스 생성
 
    try:
        rclpy.spin(node) # 노드 실행
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down and saving data...')
    finally:
        # 데이터 저장 및 종료
        node.save_data() # 저장 메서드 
        # 수정: 함수 안에서 호출 빼고 여기서 실행
        node.destroy_node() # 삭제
        rclpy.shutdown() # 종료

        # init -> spin -> 메서드 -> shutdown 


if __name__ == '__main__': 
    main()

#try except 거의 안쓰나? 얘도 연산량 많이 잡아먹음?

