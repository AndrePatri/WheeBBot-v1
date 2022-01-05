from ament_index_python.packages import get_package_share_path

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

from launch.conditions import IfCondition

def generate_launch_description():
    
    is_ign_gazebo_arg= DeclareLaunchArgument(name='ign', default_value="false",
                                     description='True if Ignition Gazebo is to be used for simulation, false (default) if Gazebo Classic is to be used instead.')                             

    package_share_path = get_package_share_path('wheebbot')

    if IfCondition(LaunchConfiguration('ign')): # changing URDF
        default_model_path = package_share_path/'description/urdf/wheebbot_ign.urdf.xacro'
    else:
        default_model_path = package_share_path/'description/urdf/wheebbot.urdf.xacro'

    default_rviz_config_path = package_share_path/'rviz/wheebbot.rviz'

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    use_sim_time_arg=DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true')

    model_arg = DeclareLaunchArgument(name='model', default_value=str(default_model_path),
                                      description='Absolute path to robot urdf file')
    rviz_arg = DeclareLaunchArgument(name='rvizconfig', default_value=str(default_rviz_config_path),
                                     description='Absolute path to rviz config file')
      

    robot_description = ParameterValue(Command(['xacro ', LaunchConfiguration('model')]),
                                       value_type=str)

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[{'use_sim_time': use_sim_time,'robot_description': robot_description}]
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
        parameters=[{'use_sim_time': use_sim_time}]
    )

    return LaunchDescription([
        is_ign_gazebo_arg,
        model_arg,
        rviz_arg,
        use_sim_time_arg,
        robot_state_publisher_node,
        rviz_node,
    ])