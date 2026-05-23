#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import SetPen
from turtlesim.msg import Pose

class request_colour(Node):
    def __init__(self):
        super().__init__("colour_client")
        self.client=self.create_client(SetPen,"change_pen_colour")

        self.pose=self.create_subscription(Pose,"/turtle1/pose",self.check_pose)
        
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("waiting for server..........")

        self.request=SetPen.Request()

        

    def check_pose(self,p):
        
        if p.x>5.5 and self.right==False:




    def send_request(self,r,g,b,w):
        self.request.r=r
        self.request.g=g
        self.request.b=b
        self.request.width=w
        self.request.off=0

        self.client.call_async(self.request)

    

def main(args=None):
    pass










def main(args=None):
    pass