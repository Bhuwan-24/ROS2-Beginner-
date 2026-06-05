from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld=LaunchDescription()

    master=Node(
        package="robo_controller",
        executable="random_rotate"
    )

    follower=Node(
        package="robo_controller",
        executable="path_follower"
    )

    ld.add_action(master)
    ld.add_action(follower)
    return ld