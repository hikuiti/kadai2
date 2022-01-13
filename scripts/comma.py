#!/usr/bin/env python2.7

import rospy
from std_msgs.msg import Int32

h = 0

rospy.init_node('comma')
pub = rospy.Publisher('comma', Int32, queue_size=1)
rate = rospy.Rate(100)

while not rospy.is_shutdown():
    h += 1
    if h%100==0:
        h = 0
    pub.publish(h)
    rate.sleep()
