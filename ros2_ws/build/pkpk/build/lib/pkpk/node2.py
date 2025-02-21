#node2
#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def sum_callback(data):
    rospy.loginfo(f"sum: {data.data}") #data: message from pub

def multiplier_publisher():
    pub = rospy.Publisher('multiplier', Int32, queue_size=10)
    rate = rospy.Rate(5)


    while not rospy.is_shutdown():
        multiplier = int(input("Enter a multiplier: "))
        rospy.loginfo(f"Publishing multiplier {multiplier}")
        pub.publish(multiplier)
        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('node2', anonymous=True) 
    rospy.Subscriber('numbers', Int32, sum_callback) 
    multiplier_publisher()
    
    
    
#합에대한 콜백함수로 펍에서 받은 합 출력
#곱 펍함수 생성해서 객체생성후 퍼블리셔생성
#반복문에서 곱할 값 입력받고 그 곱할값 출력, 객체.publish(곱할값)으로 메세지게시
#노드 직접실행했을때 이닛노드로 초기화하고 콜백함수받아서 숫자값 갱신,곱할값 펍 실행
