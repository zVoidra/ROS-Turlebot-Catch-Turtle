#!/usr/bin/env python
import time
#
import subprocess
#
from multiprocessing import Process
#
from TurtoiseClass import Turtoise
from RandomPosePublisher import RandomPosePub
from PoseEuclid import PoseEuclid

def StartTurtlesimNode():
    TurtlesimNodeName= "odev_turtlesim"
    BashCommand = "rosrun turtlesim turtlesim_node __name:=" + TurtlesimNodeName
    subprocess.run(BashCommand, shell=True)

def CreateHWTurtoise():
    TurtleName = "Turtoise_HW"
    HW = Turtoise(TurtleName, 0.5, 0.5, 0)
    HW.Spawn()

def ControlTurtoise():
    KeyboardBashCommand = "rosrun turtlesim turtle_teleop_key"
    subprocess.run(KeyboardBashCommand, shell=True)


if __name__ == "__main__":
    #Turtlesim Node
    p1 = Process(target=StartTurtlesimNode)
    p1.start()
    time.sleep(2)
    #Create [H]ome[W]ork bot
    CreateHWTurtoise()
    #Keyboard input from VSCode terminal
    p2 = Process(target=ControlTurtoise)
    p2.start()
    time.sleep(2)
    #Start Random movements for HW turtlebot
    p3 = Process(target=RandomPosePub, args=("VelocityMove",))
    p3.start()
    p4 = Process(target=RandomPosePub, args=("AngularMove",))
    p4.start()
    #Calculate Euclid Distance
    p5 = Process(target=PoseEuclid, args=("turtle1", "Turtoise_HW"))
    p5.start()
    p1.join()