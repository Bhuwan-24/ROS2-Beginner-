#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import SetPen

class set_color(Node):
    def __init__(self):
        super().__init__("colour_server")
        self.srv=self.create_service(SetPen,"change_pen_colour",self.colour)

        self.get_logger().info("service started..........")

    def colour(self,request,response):
        
        self.get_logger().info(f"r : {request.r}, g : {request.g}, b : {request.b}")

        return response
    
    def main(args=None):
        rclpy.init(args=args)
        node=set_color()
        rclpy.spin(node)
        rclpy.shutdown()
