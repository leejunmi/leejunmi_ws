import rclpy
import rclpy.node

class MinimalParam(rclpy.node.Node):
#노드클래스를 상속 -> 펍섭, 서비스 등 가능
    def __init__(self):
    #생성자에서 노드이름, 파라미터 선언, 타이머
        super().__init__('minimal_param_node')
        #부모클래스(Node)의 이닛함수 호출, 노드이름을 설정

        self.declare_parameter('my_parameter', 'world')
        #파라미터 지정
        self.timer = self.create_timer(1, self.timer_callback)
        #1초마다 초기화되어 1초에 한번 함수 실행됨, timer

    def timer_callback(self):
        my_param = self.get_parameter('my_parameter').get_parameter_value().string_value
        #파라미터값 읽고 문자열로 변환해서 my_param에 저장
        self.get_logger().info('Hello %s!' % my_param)

        my_new_param = rclpy.parameter.Parameter(
            'my_parameter',
            rclpy.Parameter.Type.STRING,
            'earth'
        )
        #새 파라미터 설정
        all_new_parameters = [my_new_param]
        self.set_parameters(all_new_parameters)
        #rclpy.parameter.Parameter의 리스트를 set_parameters에 넣어주어야함

def main():
    rclpy.init()
    node = MinimalParam() #인스턴스 생성
    rclpy.spin(node) #실행

if __name__ == '__main__':
    main()
