#!/usr/bin/env python2.7

import rospy
from std_msgs.msg import Int32

h = 0
m = 0
s = 1
c3 = 0

def cb(message):
    global h
    h = message.data

rospy.init_node('clock')
sub = rospy.Subscriber('second', Int32, cb)
pub = rospy.Publisher('clock', Int32, queue_size=1)
rate = rospy.Rate(100)

while not rospy.is_shutdown():
    m = h + 1
    if m%60 == 0:
        s += 1
    if s%100 == 0:
        c3 +=1
    if c3%60 == 0:
        c3 = 0
    pub.publish(c3)
    rate.sleep()

