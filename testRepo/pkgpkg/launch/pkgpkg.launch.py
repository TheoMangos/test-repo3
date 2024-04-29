from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pkgpkg',
            executable='Node1.py',
            name='node1'
        ),
        Node(
            package='pkgpkg',
            executable='Node2.py',
            name='node2'
        ),

        # customize launch file below
        # test
        # end launch file customization
    ])
