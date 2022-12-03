from launch_ros.actions import Node

from launch import LaunchDescription

PACKAGE_NAME = "example_pkg"

# See documentation: https://github.com/ros2/launch/blob/humble/launch/doc/source/architecture.rst
def generate_launch_description():
    pub1_node = Node(package=PACKAGE_NAME, executable="pub", name="publisher1")
    pub2_node = Node(package=PACKAGE_NAME, executable="pub", name="publisher2")
    sub_node = Node(package=PACKAGE_NAME, executable="sub", name="subscriber")

    return LaunchDescription([pub1_node, pub2_node, sub_node])
