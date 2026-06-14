from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld=LaunchDescription()

    env=Node(
        package="turtlesim",
        executable="turtlesim_node"

    )

    master=Node(
        package="robo_controller",
        executable="crash_avoid"
    )

    follower=Node(
        package="robo_controller",
        executable="path_follower"
    )
    ld.add_action(env)
    ld.add_action(master)
    ld.add_action(follower)
    return ld