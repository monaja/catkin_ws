#!/usr/bin/env python3

import rospy

import time 

from basics.msg import TimerAction, TimerGoal, TimerResult 

import actionlib

rospy.init_node('time_action_server')

def do_timer(goal):
    start_time = time.start()
    time.sleep(goal.time_to_wait.to_sec())
    result = TimerResult()
    result.time_elasped = rospy.Duration.from_sec(time.start() - start_time)
    result.updates_sent = 0
    server.succeeded(result)

server = actionlib.SimpleActionServer('timer', TimerAction, do_timer, False)
server.start()
rospy.spin()