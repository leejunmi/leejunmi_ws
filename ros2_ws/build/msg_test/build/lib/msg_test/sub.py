import rclpy
from rclpy.node import Node
from number.msg import NumNum

class Subscribe(Node):
    def __init__(self):
        super().__init__('subscribe')
        self.sub=self.create_subscription(NumNum,'topic',self.sum_callback,10)
        self.sub #??
    def sum_callback(self,msg):
        self.sum_value=msg.sum

        mul=int(input('Enter mul:'))
        result=self.sum_value*mul
        self.get_logger().info('sum*mul= %d' %result)

def main(args=None):
    rclpy.init(args=args)
    subscribe=Subscribe()
    rclpy.spin_once(subscribe) #
    rclpy.shutdown()
    
if __name__=='__main__':
    main()


