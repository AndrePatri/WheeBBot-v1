# First version of the Wheeled-Balancing-roBot

![WheeBBot](repo_images/repo_image.jpg)

## Prototype main characteristics:

- Fixed legs (no knee and, hence, no leg actuation)

- Structure made of aluminum 20x20 V-slotted profiles

- Powered by [ODrive](https://odriverobotics.com/) field-oriented controller 

- 2 BLDC ([D5065](https://eu.odriverobotics.com/shop/odrive-custom-motor-d5065)) motors and (as of now) incremental encoders  (CUI AMT102)

- 3D-printed motor housings, battery holder and cooling fan supports

- RPI 4B, 8GB RAM as the onboard computer (also provides wifi connectivity), with Ubuntu 20.04 OS and PREEMPT-RT kernel, [CAN-SPI hat](https://wiki.seeedstudio.com/2-Channel-CAN-BUS-FD-Shield-for-Raspberry-Pi/) (from Seedstudio)

- Sensing unit:

  - Encoder feedback from the axes (thorugh ODrive CAN interface)
  
  - Orientation, gyro, acc information over CAN from the on board IMU stack (made of Arduino Nano IoT/BLE sense/RP2040, sensor fusion [Adafruit BNO085](https://learn.adafruit.com/adafruit-9-dof-orientation-imu-fusion-breakout-bno085) for accurate orientation data and the older [BNO055](https://learn.adafruit.com/adafruit-bno055-absolute-orientation-sensor) which is used to get calibrated gyro readings and keep a high sensor data rate, >=100Hz). The IMU stack interfaces with the RPI using the [CAN SPI click 3.3V](https://www.mikroe.com/can-spi-33v-click) board

- 6s LiPo battery for powering the entire system

## Repo structure

- [Arduino](https://github.com/AndPatr/WheeBBot-v1/tree/main/Arduino) holds all code and custom libraries associated with the onboard microcontroller

- [CAN_databases](https://github.com/AndPatr/WheeBBot-v1/tree/main/CAN_databases) holds the used CAN databases. In particular, the one for the IMU stack interface (custom) and the ODrive (inherited)

- [RPI_Ubuntu_20.04_server](https://github.com/AndPatr/WheeBBot-v1/tree/main/RPI_Ubuntu_20.04_server) holds some files associated to the particular configuration of the used Raspberry Pi (currently 4B, 8 GB RAM)

- [ROS1_noetic/wheebbot_ws](https://github.com/AndPatr/WheeBBot-v1/tree/main/ROS1_noetic/wheebbot_ws) holds all files and workspaces associated to ROS noetic 


## (short term) ToDo

- Hardware:

 - [ ] Wire a new cable for connecting to ODrive CAN bus
 - [ ] Improve encoder connections (including the new JST pins)


- Software:

 - [ ] Test modified firmware and check the data rate is fixed and consistent
 - [ ] Plot read data on the CAN bus (both can0 and can1) using the cantools plotting utility (ODrive .dbc shouldn't need any changes)
 - [ ] Find out why Ignition isn't able to visualize the ground meshes
 - [ ] Test the connection RViz2 - Ignition (make the joint state publisher work)
 - [ ] See if env hooks can be effectively used to export Ign and Gaz. environmental variables
 - [ ] See how to load properly a gui.config in ign world file
 - [ ] Perform the pitch equilibrium angle calibration using the IMU
 - [ ] Document on Pinocchio rigid body library  
 - [ ] Outline a node structure for the ROS nodes, etc...
 - [ ] GUI for interacting with the robot (using RQt?)
 - [ ] Write a sample controller and test balancing/navigation
 
 



