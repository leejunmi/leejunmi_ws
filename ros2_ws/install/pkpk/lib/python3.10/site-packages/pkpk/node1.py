#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32 

def node1():
    pub = rospy.Publisher('numbers', Int32, queue_size=10) # ('topic name', massagetype, datasize)
    rospy.init_node('node1', anonymous=True) # master connect
    rate = rospy.Rate(5)
    
    while not rospy.is_shutdown():  # loop
        num1 = int(input("Write first number: "))
        num2 = int(input("Write second number: "))
        sum = num1 + num2
        rospy.loginfo(f"sum: {sum}")
        pub.publish(sum)  # 특정 토픽에 메세지(합) 게시하기
        rate.sleep()


     
  
    
if __name__ == '__main__':
        node1() 
   
   
   
 #토픽이름 numbers, 노드이름 node1
 #함수 안에서 1.펍객체생성해서 퍼블리셔생성(넘버스) 2.이닛노드로 초기화
 #반복문에서 넘버1,2입력받아서 합 계산하고 로그인포로 출력하고 그 합을 객체.publish로 전송함
