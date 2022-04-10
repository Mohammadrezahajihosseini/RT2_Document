#!/usr/bin/env python3
"""
.. module:: master

:platform: Unix
:synopsis: Python module for control behavior of robot

:moduleauthor: Mohammad Reza Haji Hosseini <4394567@studenti.unige.it>

This node implements an user interface ,which helps user to access different parts via shell terminal

:Master node description:
       gets user request to choose robot behaviour
       
       using robot_state rosparam
       following part:
       
       1. movebase client
       
       2. teleop keyboard
       
       3. assisted teleop
"""
import rospy
from std_srvs.srv import *
import os


def change_state():

    """
.. function:: Change_state function for changes robot's behaviour and sends the corresponding response to other three nodes, use param to change state of robot

    param userdata is the structure containing the data shared among states

    :param 1: move client
    :param 2: teleop keybord
    :param 3: assisted teleop
    :param limit: maximum number of stack frames to show
    :type limit: integer number
    :rtype: list of strings
    """
    os.system('cls||clear')
    print("** MASTER NODE **\n")

    # gets robot behaviour from user
    x = input('''Choose robot behaviour:
    1. reach point(x,y) autonomously
    2. drive with keyboard
    3. drive robot with collision avoidance\n
    input: ''')

    if x == '1':
        rospy.set_param('robot_state', '1')
        print("\nstate changed: movebase client")
    elif x == '2':
        rospy.set_param('robot_state', '2')
        print("\nstate changed: teleop keyboard")
    elif x == '3':
        rospy.set_param('robot_state', '3')
        print("\nstate changed: assisted teleop")


def main():
    """
.. function:: main function, creat initiation node for master script
    set param zero like first state of robot (User interface) 
    Start the timer with 20 Hz.
    """

    rospy.init_node('master')
    rospy.set_param('robot_state', '0')
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        if rospy.get_param('robot_state') == '0':
            change_state()
        else:
            rate.sleep()
            continue
        rate.sleep()


# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    main()
