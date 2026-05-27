#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

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
        self.pub=self.create_publisher()





def main(args=None):
    rclpy.init(args=args)
    pass


