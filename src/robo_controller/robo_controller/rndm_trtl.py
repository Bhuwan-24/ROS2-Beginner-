import rclpy
import random
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from rclpy.node import Node

class rndm_mvmt(Node):
    def __init__(self):
        super().__init__("random_movement")
        
        self.vel=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.pos=self.create_subscription(Pose,"/turtle1/pose",self.rndm_mvmt,10)
        self.rotate=0.0


    def rndm_mvmt(self,p=Pose):
        v=Twist()
        
        if p.x>9 or p.x<2 or p.y>9 or p.y<2:
            if self.rotate==0.0:
                self.rotate=random.uniform(-3,3)
            v.linear.x=1.0
            v.angular.z=self.rotate

        else:
            self.rotate=0.0
            v.linear.x=1.0
            v.angular.z=0.0
        self.vel.publish(v)

def main(args=None):
    rclpy.init(args=args)
    node=rndm_mvmt()
    rclpy.spin(node)
    rclpy.shutdown()