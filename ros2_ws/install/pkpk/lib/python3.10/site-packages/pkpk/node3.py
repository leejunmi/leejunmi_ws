#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

class ProcessorNode: 
    def __init__(self):
        self.sum_value = None
        self.multiplier = None #변수를 초기화하여 나중에 수신한 값을 저장
        self.pub = rospy.Publisher('result', Int32, queue_size=10) #펍객체만들어서 결과 퍼블리셔생성
        
        rospy.Subscriber('numbers', Int32, self.sum_callback) 
        rospy.Subscriber('multiplier', Int32, self.multiplier_callback) #숫자랑 곱할값 갱신
        
    def sum_callback(self, data):
        self.sum_value = data.data
        self.process_and_publish()

    def multiplier_callback(self, data):
        self.multiplier = data.data
        self.process_and_publish()

    def process_and_publish(self):
        if self.sum_value is not None and self.multiplier is not None: #둘다 수신되면
            result = self.sum_value * self.multiplier
            rospy.loginfo(f"result: {result}")
            self.pub.publish(result)

def main():
    rospy.init_node('processor_node', anonymous=True)
    processor = ProcessorNode()
    rospy.spin()

if __name__ == '__main__':
    main()

#메인함수에서는 노드 초기화하고 클래스의 객체 생성(안에서 이닛메서드 수행하고 펍섭 설정됨)




