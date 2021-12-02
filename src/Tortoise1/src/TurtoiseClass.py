#!/usr/bin/env python

#Library to run bash commands with python file
import subprocess

class Turtoise:

    def __init__(self, TurtleName, xLocation, yLocation, thetaLocation):
        self.TurtleName = TurtleName
        self.xLocation = xLocation
        self.yLocation = yLocation
        self.thetaLocation = thetaLocation 
    
    def Spawn(self):
        SpawnBashCommand = ("rosservice call /spawn "
        + str(self.xLocation) + " " + str(self.yLocation) + " "  + str(self.thetaLocation) 
        + " "  + self.TurtleName)
        subprocess.run(SpawnBashCommand, shell=True, check=True) 
