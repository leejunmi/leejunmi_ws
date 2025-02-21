import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from cv_bridge import CvBridge
import cv2
from sensor_msgs.msg import Image
import numpy as np

bridge=CvBridge()

class camSub(Node):
    def __init__(self):
        super().__init__('sub') # 노드이름 'sub'
        qos=QoSProfile(depth=10) #안하면 오류남
        self.sub=self.create_subscription(Image, 'cam_img',self.image_callback,qos)
        #
        self.sub
        self.image=np.empty(shape=[1]) # 클래스의 속성으로 저장되어 여러 메서드에서 사용되는 변수를 self.변수로 담아줘야함

    def image_callback(self,data):
        self.image=bridge.imgmsg_to_cv2(data, desired_encoding='rgb8') 
        #
        cv2.imshow('img',self.image)
        cv2.waitKey(33) #숫자 담아줘야헤
     
def main(args=None):
    rclpy.init(args=args)
    node=camSub()
    try:
        rclpy.spin(node) #인스턴스 넣기
    except KeyboardInterrupt:
        node.get_logger().info('stop by keyboard')
    finally:
        node.destroy_node()
        rclpy.shutdown()
if __name__=='__main__':
    main()


