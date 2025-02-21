import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        # 부모 클래스(Node)의 __init__ 호출, 노드 이름을 'my_node'로 설정
        super().__init__('my_node')  
        self.get_logger().info("Node has been initialized!")

def main(args=None):
    rclpy.init(args=args)  # ROS 2 초기화
    node = MyNode()        # 노드 생성
    rclpy.spin(node)       # 노드 실행
    node.destroy_node()    # 노드 종료
    rclpy.shutdown()       # ROS 2 종료

if __name__ == '__main__':
    main()
