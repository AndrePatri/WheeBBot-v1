from ament_index_python.packages import get_package_share_path

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument

from launch.substitutions import Command, LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    package_share_path = get_package_share_path('wheebbot')
    default_model_path = package_share_path/'description/urdf/wheebbot.urdf.xacro'
    default_rviz_config_path = package_share_path/'rviz/wheebbot.rviz'

    model_arg = DeclareLaunchArgument(name='model', default_value=str(default_model_path),
                                      description='Absolute path to robot urdf file')
    rviz_arg = DeclareLaunchArgument(name='rvizconfig', default_value=str(default_rviz_config_path),
                                     description='Absolute path to rviz config file')
    is_sim_time_arg= DeclareLaunchArgument(name='use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true')

    robot_description = ParameterValue(Command(['xacro', LaunchConfiguration('model')]),
                                       value_type=str)
                                    

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'use_sim_time': use_sim_time,'robot_description': robot_description}]
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
    )

    return LaunchDescription([
        model_arg,
        rviz_arg,
        is_sim_time_arg,
        robot_state_publisher_node,
        rviz_node
    ])