# main.py
# Author: Daniel D'Souza
# Drive a robot with leap motion.

import sys

import vrep as v
from pioneer_async import PioneerAsync
from virtual_joy import JoyListener, get_virtual_joystick
import numpy as np
import math

v.simxFinish(-1)  # just in case, close all opened connections
clientID = v.simxStart('127.0.0.1', 19997, True, True, 5000, 5)  # Connect to V-REP

if clientID == -1:
    print('Could not connect to V-REP')
    quit()

print('Successfully connected to V-REP')
robot1 = PioneerAsync(clientID)
robot1.set_motors(0.0, 0.0)


def method(input):
    x, y = input[0], input[2]
    # print(x, y)

    x_norm = -x / math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    y_norm = y / math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    print(x_norm, y_norm)
    #
    # robot1.set_motors(0.1, 0.1)
    print('left', y*0.02 + 0*x*0.01)
    print('right', y*0.02 - 0*x*0.01)

    robot1.set_motors(y*0.01 + x*0.01, y*0.01 - x*0.01)

controller, l = get_virtual_joystick(method)

# listener = JoyListener()
# controller = Leap.Controller()
# controller.add_listener(listener)

# start simulation
# v.simxStartSimulation(clientID, v.simx_opmode_oneshot)

print('Press ENTER to quit.')
try:
    sys.stdin.readline()
except KeyboardInterrupt:
    pass
finally:
    controller.remove_listener(l)
