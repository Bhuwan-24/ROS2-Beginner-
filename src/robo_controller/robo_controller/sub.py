#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class sub_pose(Node):
    def __init__(self):
        super().__init__("turtle_pose")
        self.sub=self.create_subscription(Pose,"/turtle1/pose",self.pos_callback,10)

    def pos_callback(self,msg:Pose):
        self.get_logger().info(str(msg))


def main(args=None):
    rclpy.init(args=args)
    node=sub_pose()
    rclpy.spin(node)
    rclpy.shutdown()