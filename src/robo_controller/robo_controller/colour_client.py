#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import SetPen
from turtlesim.msg import Pose

class request_colour(Node):
    def __init__(self):
        super().__init__("colour_client")
        self.client=self.create_client(SetPen,"/turtle1/set_pen")

        self.pose=self.create_subscription(Pose,"/turtle1/pose",self.check_pose,10)
        
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("waiting for server..........")

        self.request=SetPen.Request()
        self.right=False

        

    def check_pose(self,p):
        
        if p.x>5.5 and not self.right:
            self.send_request(255,0,0,5)
            self.get_logger().info("red colour")
            self.right=True

        elif p.x<5.5 and self.right:
            self.send_request(0,0,255,5)
            self.get_logger().info("blue colour")
            self.right=False


    def send_request(self,r,g,b,w):
        self.request.r=r
        self.request.g=g
        self.request.b=b
        self.request.width=w
        self.request.off=0
        self.client.call_async(self.request)

    

def main(args=None):
    rclpy.init(args=args)
    node=request_colour()
    rclpy.spin(node)
    rclpy.shutdown()

