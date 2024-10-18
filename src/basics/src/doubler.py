#!/usr/bin/env python3

import rospy

from std_msgs.msg import Int32 

rospy.init_node('doubler')

def callback(msg):
    doubled = Int32()
    number = msg.data
    print("data received: ")
    print(number)
    doubled = number * 2
    print("data doubled: ")
    print(doubled)
    pub.publish(doubled)

sub = rospy.Subscriber('number', Int32, callback)
pub = rospy.Publisher('doubled', Int32)

rospy.spin()