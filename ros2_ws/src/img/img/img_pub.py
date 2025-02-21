import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
import cv2
from sensor_msgs.msg import Image

bridge=CvBridge() # 객체 생성

class camPub(Node):
    def __init__(self):
        super().__init__('pub') #노드이름 pub
        self.publisher=self.create_publisher(Image,'cam_img',10)
        time_period=0.1
        self.timer=self.create_timer(time_period,self.time_callback) #주어진 함수를 일정한 시간간격으로 실행하기 위함
        self.cap=cv2.VideoCapture(0)

    def time_callback(self):
        ret,frame=self.cap.read()
        #cv2.imwrite('test.jpg',frame) #이름을 계속 덮어쓰기 때문에 한장만 저장 ->없어도됨?
        if ret==True:
            fra=bridge.cv2_to_imgmsg(frame,encoding='bgr8')
            self.publisher.publish(fra) #self 안써도됨???
            cv2.imshow('frame',frame)
            cv2.waitKey(1)
        self.get_logger().info('publish img')
def main(args=None):
    rclpy.init(args=args)
    node=camPub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('publish stop')
    finally:
        node.destroy_node()
        rclpy.shutdown()
if __name__=='__main__': #위치
    main()



        

