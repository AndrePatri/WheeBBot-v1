cmake_minimum_required(VERSION 3.1.3)
project(wheebbot)

find_package(catkin REQUIRED COMPONENTS roscpp rospy urdf sensor_msgs xbot_msgs)

catkin_package()

include_directories(include ${catkin_INCLUDE_DIRS})

add_executable()
target_link_libraries( ${catkin_LIBRARIES})

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(DIRECTORY worlds DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(DIRECTORY media DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(DIRECTORY description/sdf DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(DIRECTORY description/urdf DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(DIRECTORY description/srdf DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(DIRECTORY description/meshes DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

