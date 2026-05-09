import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class draw_circle(Node):

    def __init__(self):
        super().__init__("turtle_circle")
        self.vel=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        timer=self.create_timer(0.5,self.cmd_vel)
        self.get_logger().info("Turtle is rotating")

    def cmd_vel(self):
        msg=Twist()
        msg.linear.x=5.0
        msg.angular.z=1.0
        self.vel.publish(msg)




def main(args=None):
    rclpy.init(args=args)

    node=draw_circle()
    rclpy.spin(node)

    rclpy.shutdown()