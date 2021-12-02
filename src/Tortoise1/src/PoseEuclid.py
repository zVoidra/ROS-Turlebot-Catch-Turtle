#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
#
from multiprocessing import Process
#
import math

class PoseEuclid:

    T1Pose = Pose
    T2Pose = Pose

    def __init__(self, T1Name, T2Name):
        self.T1Node(T1Name)
        self.T2Node(T2Name)
        rospy.spin()

    def T1Node(self, turtlename):
        rospy.init_node('PoseListener', anonymous=True)
        TurtleTopic = '/'+turtlename+'/pose'
        rospy.Subscriber(TurtleTopic, Pose, self.T1Callback)

    def T2Node(self, turtlename):
        rospy.init_node('PoseListener', anonymous=True)
        TurtleTopic = '/'+turtlename+'/pose'
        rospy.Subscriber(TurtleTopic, Pose, self.T2Callback)

    def T1Callback(self, inData):
        self.T1Pose = inData
        self.CalculateEuclid()

    def T2Callback(self, inData):
        self.T2Pose = inData
        self.CalculateEuclid()

    def CalculateEuclid(self):
        #Euclid Calculation

        EuclidDistance = math.sqrt(pow((self.T2Pose.x - self.T1Pose.x),2) + pow((self.T2Pose.y - self.T1Pose.y),2))
        if EuclidDistance < (0.5):
            print("GAMEOVER")