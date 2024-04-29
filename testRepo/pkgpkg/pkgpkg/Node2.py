#!/usr/bin/env python3
# Note: the file will only save edits in the designated locations
# editable locations are denoted by comments. DO NOT remove the
# generated comments
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8

from pkgpkg.srv import (Service1, GoalService)

# add custom imports below
# no
# end custom imports


class Node2(Node):

    def __init__(self):
        super().__init__('node2')
        self.topic1_pub = self.create_publisher(Int8, '/Topic1', 10)
        self.service1_client = self.create_client(Service1, 'service1')
        while not self.service1_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service1 Service not available, waiting again...')
        self.goal_service_client = self.create_client(
            GoalService, 'goal_service')
        while not self.goal_service_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('GoalService Service not available, waiting again...')

        # customize init function below
        # yes
        # end init customization

    # add custom methods to the node below
    # yes
    # end custom methods


def main(args=None):
    # customize main function below
    # Note: editing any of the generated code here could break the node.
    # take precaution when editing
    rclpy.init(args=args)
    # guess
    node2 = Node2()

    rclpy.spin(node2)

    node2.destroy_node()
    rclpy.shutdown()
    # end main customization


if __name__ == '__main__':
    main()
