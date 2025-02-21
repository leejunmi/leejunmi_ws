# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node #노드 클래스 가져옴

from tutorial_interfaces.msg import Num #문자열메세지 주고받기 위해 사용


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher') 
        #클래스 생성자 호출? minimal_publisher가 실행될때 초기화 , 노드이름은minimalPublisher
        self.publisher_ = self.create_publisher(Num, 'topic', 10) #string타입의 publisher객체 생성

#퍼블리셔 객체 생성
#publisher=node.create_publisher(msgtype,topic_name, qos_depth)

        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback) #주기마다 self.timer_callback메서드 호출
#
        self.i = 0

    def timer_callback(self):
        msg = Num() #string형식으로 msg생성
        msg.num =self.i #출력할메세지데이터 설정
        self.publisher_.publish(msg) #메세지를 퍼블리셔를 통해 발행
  #publisher.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.num)
  #node.get_logger().info(출력할 info 메세지)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher() #minimal_publisher노드 생성?

    rclpy.spin(minimal_publisher) #이벤트루프 시작

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()
    
 #메인함수:rclpy 라이브러리가 초기화되고, 노드가 생성되고, 노드를 spin하여 콜백 호출됨


if __name__ == '__main__':
    main()
