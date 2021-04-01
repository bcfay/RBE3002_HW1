import numpy
import pandas as pd
import math
from pip._vendor.distlib.compat import raw_input

# generates linear speed from a wheels diameter and rpm
# rpm is revolutions per minute
# diameter is in m
# returns speed in m/s
def vel_gen(vel, diameter):
    r = diameter / 2
    rad_p_sec = vel / r
    rpm = rad_p_sec * (2 * math.pi) / 60
    return rpm


def Turtlebot_vel_gen(vel):
    Turtlebot_d = .065  # in M
    return vel_gen(vel, Turtlebot_d)

def p5_control(vel, dir, ICC = 0):
    if(ICC == 0):
        rpm = Turtlebot_vel_gen(vel)
        if(dir == 'F'):
            return "( " + str(mean_val) + ", " + str(var_val) + ")")


    else:





max_vel = .22 #m/s
x = 0;
while (x != 'q'):
    print("")
    print("Exit with 'q'")
    print("Enter Turtlebot velocity:")
    x = raw_input()
    if(x == 'q'):
        continue
    try:
        val = float(x)
        if (val > max_vel):
            print("Invalid Velocity Request!")
            continue
        print("Turtlebot rpm:")
        print(Turtlebot_vel_gen(val))
    except ValueError:
        print("That's not a valid rpm.")


