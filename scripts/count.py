#!/usr/bin/env python2.7
import rospy
import sys
from std_msgs.msg import Int32

sys.path.append('/home/ubuntu/.local/lib/python2.7/site-packages')

import rospkg

rospy.init_node('count') 
pub = rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(10) 
n = 0
while not rospy.is_shutdown():
    n += 1
    pub.publish(n)
    rate.sleep()
