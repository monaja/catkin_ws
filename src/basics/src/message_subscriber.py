#!/usr/bin/env python3

import rospy

from basics.msg import Complex 

rospy.init_node('message_subscriber')

def callback(msg):
    print("Real: ")
    print(msg.real)
    print("Imaginary: ")
    print(msg.imaginary)
    print("")

sub = rospy.Subscriber('complex', Complex, callback)

rospy.spin()

