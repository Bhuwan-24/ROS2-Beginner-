#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class add_client(Node):
    def __init__(self):
        super().__init__("add_client")
        self.client=self.create_client(AddTwoInts,"add_here")

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("waiting for server")
        
        self.request=AddTwoInts.Request()

    def send_request(self,a,b):
        self.request.a=a
        self.request.b=b
        future =self.client.call_async(self.request)
        rclpy.spin_until_future_complete(self,future)
        return future.result()



def main(args=None):
    rclpy.init(args=args)
    client=add_client()
    response=client.send_request(5,2)
    client.get_logger().info(f"Response : {response.sum}")
    rclpy.shutdown()
    
    