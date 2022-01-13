#!/usr/bin/env python2.7

import rospy
from std_msgs.msg import Int32

h = 0
m = 0
c2 = 0

def cb(message):
    global h
    h = message.data

rospy.init_node('second')
sub = rospy.Subscriber('comma', Int32, cb)
pub = rospy.Publisher('second', Int32, queue_size=1)
rate = rospy.Rate(100)

while not rospy.is_shutdown():
    m = h + 1
    if m%100 == 0:
        c2 += 1
    if c2%60 == 0:
        c2 = 0
    pub.publish(c2)
    rate.sleep()
