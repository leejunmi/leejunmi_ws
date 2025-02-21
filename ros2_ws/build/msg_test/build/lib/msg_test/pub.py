import rclpy
from rclpy.node import Node
from number.msg import NumNum 

class Publish(Node):

    def __init__(self):
        super().__init__('publish') #노드이름 publish로
        self.publisher=self.create_publisher(NumNum, 'topic',10)
        #펍 객체 생성(publisher)
    def calculate(self):
        a=int(input('Enter a: '))
        b=int(input('Enter b: '))
        sum=a+b

        msg=NumNum()
        msg.a=a
        msg.b=b
        msg.sum=sum

        self.publisher.publish(msg) #msg게시
        self.get_logger().info('Publishing: sum=%d ' %msg.sum) 

def main(args=None):
    rclpy.init(args=args) #노드생성하기 위해서는  init필수.

    publish=Publish() #퍼블리시 클래스의 인스턴스 생성
    publish.calculate() #call calculate
    rclpy.spin_once(publish)  #rclpy.spin_once(node이름)
    #spin없으면 콜백이 안 됨, 구독자가 받기 전에 함수가 종료될 수 있음. (sub,timer등 )
    rclpy.shutdown() 

if __name__=='__main__':
    main()

#'topic'이름의 토픽을 publish노드에서 subscribe노드로 보냄. 
#펍 객체 생성할 때 전송할 메세지타입과 토픽이름을 넣어줌.
#msg객체에 메세지타입을 넣어주고
#노드이름.publish(msg)로 퍼블리시하기!


