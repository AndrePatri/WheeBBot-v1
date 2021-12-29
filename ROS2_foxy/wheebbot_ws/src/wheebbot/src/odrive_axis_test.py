#!/usr/bin/env python3

##################### Imports #########################

import odrive 
from odrive.enums import *

# import rospy
# import rospkg

import time

##################### Reading the YAML config file #########################

# brake_res = rospy.get_param("/odrive/config/brake_resistance") 
# dc_max_negative_current= rospy.get_param("/odrive/config/dc_max_negative_current") 
# max_regen_current= rospy.get_param("/odrive/config/max_regen_current") 

# axis0_startup_encoder_index_search= rospy.get_param("/odrive/axis0/config/startup_encoder_index_search")
# axis0_node_id= rospy.get_param("/odrive/axis0/config/can/node_id")
# axis0_encoder_rate_ms= rospy.get_param("/odrive/axis0/config/can/encoder_rate_ms")
# axis0_heartbeat_rate_ms= rospy.get_param("/odrive/axis0/config/can/heartbeat_rate_ms")
# axis0_current_lim= rospy.get_param("/odrive/axis0/motor/config/current_lim")
# axis0_pole_pairs= rospy.get_param("/odrive/axis0/motor/config/pole_pairs")
# axis0_torque_constant= rospy.get_param("/odrive/axis0/motor/config/torque_constant")
# axis0_calibration_current= rospy.get_param("/odrive/axis0/motor/config/calibration_current")
# axis0_resistance_calib_max_voltage= rospy.get_param("/odrive/axis0/motor/config/resistance_calib_max_voltage")
# axis0_motor_pre_cal= rospy.get_param("/odrive/axis0/motor/config/pre_calibrated")
# axis0_encoder_cpr= rospy.get_param("/odrive/axis0/encoder/config/cpr")
# axis0_encoder_mode= rospy.get_param("/odrive/axis0/encoder/config/mode")
# axis0_encoder_cal_range= rospy.get_param("/odrive/axis0/encoder/config/calib_range")
# axis0_encoder_pre_cal= rospy.get_param("/odrive/axis0/encoder/config/pre_calibrated")
# axis0_input_mode= rospy.get_param("/odrive/axis0/controller/config/input_mode")
# axis0_cntrl_mode= rospy.get_param("/odrive/axis0/controller/config/control_mode")
# axis0_vel_lim= rospy.get_param("/odrive/axis0/controller/config/vel_limit")

# axis1_startup_encoder_index_search= rospy.get_param("/odrive/axis1/config/startup_encoder_index_search")
# axis1_node_id= rospy.get_param("/odrive/axis1/config/can/node_id")
# axis1_encoder_rate_ms= rospy.get_param("/odrive/axis1/config/can/encoder_rate_ms")
# axis1_heartbeat_rate_ms= rospy.get_param("/odrive/axis1/config/can/heartbeat_rate_ms")
# axis1_current_lim= rospy.get_param("/odrive/axis1/motor/config/current_lim")
# axis1_pole_pairs= rospy.get_param("/odrive/axis1/motor/config/pole_pairs")
# axis1_torque_constant= rospy.get_param("/odrive/axis1/motor/config/torque_constant")
# axis1_calibration_current= rospy.get_param("/odrive/axis1/motor/config/calibration_current")
# axis1_resistance_calib_max_voltage= rospy.get_param("/odrive/axis1/motor/config/resistance_calib_max_voltage")
# axis1_motor_pre_cal= rospy.get_param("/odrive/axis1/motor/config/pre_calibrated")
# axis1_encoder_cpr= rospy.get_param("/odrive/axis1/encoder/config/cpr")
# axis1_encoder_mode= rospy.get_param("/odrive/axis1/encoder/config/mode")
# axis1_encoder_cal_range= rospy.get_param("/odrive/axis1/encoder/config/calib_range")
# axis1_encoder_pre_cal= rospy.get_param("/odrive/axis1/encoder/config/pre_calibrated")
# axis1_input_mode= rospy.get_param("/odrive/axis1/controller/config/input_mode")
# axis1_cntrl_mode= rospy.get_param("/odrive/axis1/controller/config/control_mode")
# axis1_vel_lim= rospy.get_param("/odrive/axis1/controller/config/vel_limit")

##################### Reading the YAML config file #########################

# Find a connected ODrive (this will block until you connect one)
print("finding an odrive...")
my_odrive = odrive.find_any()

# Calibrate motor and wait for it to finish
print("starting calibration...")
my_odrive.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
my_odrive.axis1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE

while (my_odrive.axis0.current_state != AXIS_STATE_IDLE) or (my_odrive.axis1.current_state != AXIS_STATE_IDLE):
    time.sleep(0.1)

my_odrive.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
my_odrive.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

# To read a value, simply read the property
print("Bus voltage is " + str(my_odrive.vbus_voltage) + "V")

time.sleep(5)

my_odrive.axis0.requested_state = AXIS_STATE_IDLE
my_odrive.axis1.requested_state = AXIS_STATE_IDLE

my_odrive.save_configuration()