#!/usr/bin/env python3
# Note: the file will only save edits in the designated locations
# editable locations are denoted by comments. DO NOT remove the
# generated comments
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8

from pkgpkg.srv import ( Service1, GoalService)

# add custom imports below

# end custom imports

class Node1(Node):

    def __init__(self):
        super().__init__('node1')
        self.topic1_sub = self.create_subscription(Int8, '/Topic1', self.topic1_callback, 10)
        self.service1_server = self.create_service(Service1, 'service1', self.service1_srv_callback)
        self.goal_service_server = self.create_service(GoalService, 'goal_service', self.goal_service_srv_callback)

        # customize init function below

        # end init customization

    def topic1_callback(self, msg):
        # add topic1_callback implementation below 
        pass
        # end topic1_callback implementation
    
    def service1_srv_callback(self, request, response):
        # add service1_srv_callback implementation below
        return response

        # end service1_srv_callback implementation
    def goal_service_srv_callback(self, request, response):
        # add goal_service_srv_callback implementation below
        return response

        # end goal_service_srv_callback implementation



    # add custom methods to the node below

    # end custom methods

def main(args=None):
    # customize main function below
    # Note: editing any of the generated code here could break the node.
    # take precaution when editing
    rclpy.init(args=args)

    node1 = Node1()

    rclpy.spin(node1)

    node1.destroy_node()
    rclpy.shutdown()
    # end main customization


if __name__ == '__main__':
    main()
