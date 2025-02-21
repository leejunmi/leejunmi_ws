import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
import sensor_msgs_py.point_cloud2 as pc2
import open3d as o3d
import numpy as np

class BagToPCD(Node):
    def __init__(self):
        super().__init__('bag_to_pcd')
        self.subscription = self.create_subscription(
            PointCloud2,
            '/points',  # PointCloud2 데이터 토픽 이름
            self.pointcloud_callback,
            10
        )
        self.pcd_index = 0

    def pointcloud_callback(self, msg):
        point_cloud = np.array(list(pc2.read_points(msg, skip_nans=True, field_names=("x", "y", "z"))))

        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(point_cloud)

        # PCD 파일로 저장
        filename = f"pointcloud_{self.pcd_index:04d}.pcd"
        o3d.io.write_point_cloud(filename, pcd)
        self.get_logger().info(f"Saved {filename}")
        self.pcd_index += 1

def main(args=None):
    rclpy.init(args=args)
    bag_to_pcd = BagToPCD()
    rclpy.spin(bag_to_pcd)
    bag_to_pcd.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
