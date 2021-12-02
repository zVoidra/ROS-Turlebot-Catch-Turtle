#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
import random

from multiprocessing import Process
#
TwistMessage = Twist()
PubNode = rospy.Publisher('/Turtoise_HW/cmd_vel', Twist, queue_size=10)

class RandomPosePub:

    def __init__(self, type):
        rospy.init_node('move_turtle', anonymous=True)
        if type == "AngularMove":
            self.AngularVelocity()
        elif type == "VelocityMove":
            self.LinearVelocity() 
    
    def LinearVelocity(self):
        rate = rospy.Rate(0.5)#2 saniyede 1

        while not rospy.is_shutdown():
            TwistMessage.linear.x = random.uniform(0, 3)
            PubNode.publish(TwistMessage)
            rate.sleep()

    def AngularVelocity(self):
        rate = rospy.Rate(0.2)# 5 saniyede 1

        while not rospy.is_shutdown():
            TwistMessage.angular.z = random.uniform(0, 0.5)
            PubNode.publish(TwistMessage)
            rate.sleep()

    


