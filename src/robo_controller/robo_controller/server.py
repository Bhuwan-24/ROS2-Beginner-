#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class add_server(Node):
    def __init__(self):
        super().__init__("add_server")
        self.service=self.create_service(AddTwoInts,"add_here",self.add_callback)
        self.get_logger().info("Service Started...............")

    def add_callback(self,request,response):
        response.sum=request.a+request.b
        self.get_logger.info(f"{request.a} + {request.b} = {response.sum}")

def main(args=None):
    rclpy.init(args=args)
    node=add_server()
    rclpy.spin(node)
    rclpy.shutdown()