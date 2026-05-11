#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class smart_turtle(Node):
    def __init__(self):
        super().__init__("border_avoid")
        self.get_logger().info("Starting of node....")
        self.pub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.sub=self.create_subscription(Pose,"/turtle1/pose",self.pos,10)

    def pos(self,p=Pose):
        
        vel=Twist()

        if p.x>9 or p.x<2 or p.y>9 or p.y<2:
            self.get_logger().info("border detected.......")
            vel.linear.x=0.5
            vel.angular.z=0.9
            self.get_logger().info(str(vel.angular.x))

        else:
            self.get_logger().info("moving.......")
            vel.linear.x=2.0
            vel.angular.x=0.0

        self.pub.publish(vel)

def main(args=None):
    rclpy.init(args=args)
    node=smart_turtle()
    rclpy.spin(node)
    rclpy.shutdown()
