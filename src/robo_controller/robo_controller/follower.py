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


    def call_turtle(self,x,y,theta,name):
        self.request.x=x
        self.request.y=y
        self.request.theta=theta
        self.request.name=name
        return self.new.call_async(self.request)

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
            self.cord.append([self.mx,self.my])
        last_cord=self.cord[-1]
        apnd=np.sqrt((self.mx-last_cord[0])**2+(self.my-last_cord[1])**2)
        if apnd>1:
            self.cord.append([self.mx,self.my])

    def path_follow(self,p:Pose):
        vel=Twist()
        cx=p.x
        cy=p.y
        ct=p.theta
        if len(self.cord)==0:
            return
        target_pos=self.cord[0]
        dist=np.sqrt((cx-target_pos[0])**2+(cy-target_pos[1])**2)
        target_ang=np.arctan2(target_pos[1]-cy,target_pos[0]-cx)
        diff=target_ang-ct
        ang_diff=np.arctan2(np.sin(diff),np.cos(diff))
        if abs(ang_diff)>0.5:
            vel.angular.z=1*ang_diff
            vel.linear.x=0.2

        else:
            vel.linear.x=min(0.9*dist,2.0)
            vel.angular.z=0.3*ang_diff

        if dist<0.5 and len(self.cord)>1:
            self.cord.popleft()

        self.pub.publish(vel) 
       


def main(args=None):
    rclpy.init(args=args)
    node1=new_turtle()
    future=node1.call_turtle(5.5,5.5,0.0,"turtle2")
    rclpy.spin_until_future_complete(node1,future)
    node1.destroy_node()
    node2=follow()
    rclpy.spin(node2)
    rclpy.shutdown()
    


