# First version of the Wheeled-Balancing-roBot

![WheeBBot](https://github.com/AndPatr/github_repo_images/blob/main/WheeBBot-v1/wheebbot_repo_image_compressed-min.jpg)

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


## ToDo

- [ ] Obtain an URDF representation of the robot

- [ ] Perform the pitch equilibrium angle calibration using the IMU

- [ ] Write the full floating base model of the system (possibly using Matlab's symbolic language), to be used by the controller. Also check if using RBDL or similar can be viable

- [x] Test torque commands and encoder feedback to/from ODrive through CAN  

- [x] Possibly modify ODrive firmware to also return the measured i_d current on both axes

- [ ] Modify ODrive firmware so that the position, velocity and torque commands have higher ID priority than the heartbeat and the feedback from the axis (simply swap cmd ids in can_simple.hpp and modify them in create_can_dbc.py)

- [ ] Flash firmware on the ODrive and test if it works properly (double check if the tup.config file has the correct board version set)

- [ ] Write a node which reads IMU data on can1 bus and wheel encoders data on can0 and publishes it (with possible post-processing) to a WheeBBot_state topic. Initially employ python scripts and the .dbc files. In a second phase, explore the possibility of using more efficient c++ code which interfaces with SocketCAN

- [ ] Write a GUI for visualizing data from the sensors and possibly also interacting with the robot

- [ ] See if it is possible to include current feedback into the sent messages in the ODrive

- [ ] Setup a controller (possibly a service) node, which reads the full state, the output references and publishes the desired control inputs. This node should hold the controller script to be tested on the robot and should be written in a modular way, in a way that different control inputs can be integrated easily. This node could also be deployed on the host pc so that the RPI is lifted from the computational burden. 

- [ ] Write a node which, given the computed inputs, sends the control inputs on can0 to the ODrive (torques)
	  
- [ ] Writing a sample controller. Ideally it should be made of a two stage controller: an higher level one (kinematic), which takes velocity references (for example of the CoM) and a lower level one, which translates those references into the joint space.

- [ ] Writing a node (to be run on a host pc) which reads output references published by an USB joystick (Xbox360) and sends high level references to the controller node on the RPI.

- [ ] Testing the real-time performance of the system without actuating the robot (if necessary, switch to Xenomai)

- [ ] Testing the effectiveness of balancing/navigation

- [ ] Moving to v2

Possible hardware improvements:

  - [ ] Test the performance of the RP2040 w.r.t. the Nano IoT
  
  - [ ] Absolute encoders
  
  - [ ] Deploy the controller on an additional microcontroller to improve RT performance?
 



