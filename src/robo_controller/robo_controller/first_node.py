#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class mynode(Node):

    def __init__(self):
        super().__init__("mynode")
        self.create_timer(1.0,self.timer_call())
        
    def timer_call(self):
        self.get_logger.info("Hello world")


def main(args=None):
    rclpy.init(args=args)

    node=mynode()
    rclpy.spin(node)

    rclpy.shutdown()




if __name__=='__main__':
    main()