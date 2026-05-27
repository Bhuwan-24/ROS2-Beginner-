#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from collections import deque
import numpy as np

class new_turtle(Node):
    
    def __init__(self):
        super().__init__("new_turtle")
        self.new=self.create_client(Spawn,"/spawn")
        while not self.new.wait_for_service(1.0):
            self.get_logger().info("waiting for server........................")
        
        self.request=Spawn.Request()


    def call_turtle(self,x,y,theta):
        self.request.x=x
        self.request.y=y
        self.request.theta=theta
        self.new.call_async(self.request)

class follow(Node):
    def __init__(self):
        super().__init__("follower")
        self.pub=self.create_publisher(Twist,"/turtle2/cmd_vel",10)
        self.m_pos=self.create_subscription(Pose,"/turtle1/pose",self.master_pose,10)
        self.c_pos=self.create_subscription(Pose,"/turtle2/pose",self.path_follow,10)
        self.cord=deque()

    def master_pose(self,p:Pose):
        self.mx=p.x
        self.my=p.y
        self.mt=p.theta
        if len(self.cord)==0:
            self.cord.append([self.mx,self.my,self.mt])

    def path_follow(self,p:Pose):
        cx=p.x
        cy=p.y
        ct=p.theta
        l=self.cord.pop()

        apnd_condn=np.sqrt((self.mx-l[0])**2-(self.my-l[1])**2)
        if apnd_condn>1.0:
            self.cord.append([self.mx,self.my,self.mt])
        target_pos=self.cord.popleft()
        dist=np.sqrt((cx-target_pos[0])**2-(cy-target_pos[1])**2)
        diff=target_pos[2]-ct
        ang_diff=np.arctan2tan(np.sin(diff),np.cos(diff))
        

        







def main(args=None):
    rclpy.init(args=args)
    pass


