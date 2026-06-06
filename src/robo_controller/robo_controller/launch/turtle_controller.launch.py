from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    lnch=LaunchDescription()

    trtl=Node(
        package="turtlesim",
        executable="turtlesim_node"
    )

    control=Node(
        package="turtlesim",
        executable="turtle_teleop_key",
        output='screen',
        prefix="xterm -e"
    )
    
    lnch.add_action(trtl)
    lnch.add_action(control)
    return lnch
