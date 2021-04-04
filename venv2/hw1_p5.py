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
    return numpy.round(rpm,2)


def Turtlebot_rpm_gen(vel):
    Turtlebot_d = .065  # in M
    return vel_gen(vel, Turtlebot_d)


def p5_control(vel, dir, ICC=None):
    CTC = .156

    if (ICC == None):
        rpm = Turtlebot_rpm_gen(vel)
        rpm = numpy.round(rpm, 2)
        if (dir == 'F'):
            return ("( " + str(rpm) + ", " + str(rpm) + ")")
        if (dir == 'R'):
            return ("( " + str((-1)*rpm) + ", " + str((-1)*rpm) + ")")
        else:
            print("invalid direction")
            return ("( " + str(0) + ", " + str(0) + ")")
    if (ICC == 0):
        rpm = Turtlebot_rpm_gen(vel)
        rpm = numpy.round(rpm, 2)
        if (dir == 'F'):
            return ("( " + str(rpm) + ", " + str((-1)*rpm) + ")")
        if (dir == 'R'):
            return ("( " + str((-1)*rpm) + ", " + str(rpm) + ")")
        else:
            print("invalid direction")
            return ("( " + str(0) + ", " + str(0) + ")")
    if (ICC > 0):
        if (ICC > CTC):
            omega = vel/ICC
            inside_vel = omega*(ICC-(CTC/2))
            outside_vel = omega*(ICC+(CTC/2))
            inside_vel = numpy.round(inside_vel, 2)
            outside_vel = numpy.round(outside_vel, 2)

            if (dir == 'F'):
                return ("( " + str(Turtlebot_rpm_gen(outside_vel)) + ", " + str(Turtlebot_rpm_gen(inside_vel)) + ")")
            if (dir == 'R'):
                return ("( " + str((-1)*Turtlebot_rpm_gen(outside_vel)) + ", " + str((-1)*Turtlebot_rpm_gen(inside_vel)) + ")")
            else:
                print("invalid direction")
                return ("( " + str(0) + ", " + str(0) + ")")
        else: #inside wheels
            omega = vel / ICC
            inside_vel = omega * ((CTC / 2) - ICC)
            outside_vel = omega * ((CTC / 2) + ICC)
            inside_vel = numpy.round(inside_vel, 2)
            outside_vel = numpy.round(outside_vel, 2)

            if (dir == 'F'):
                return ("( " + str(Turtlebot_rpm_gen(outside_vel)) + ", " + str((-1)*Turtlebot_rpm_gen(inside_vel)) + ")")
            if (dir == 'R'):
                return ("( " + str((-1)*Turtlebot_rpm_gen(outside_vel)) + ", " + str(Turtlebot_rpm_gen(inside_vel)) + ")")
            else:
                print("invalid direction")
                return ("( " + str(0) + ", " + str(0) + ")")
    if(ICC < 0):
        if (ICC > CTC):
            omega = vel / ICC
            inside_vel = omega * (ICC - (CTC / 2))
            outside_vel = omega * (ICC + (CTC / 2))
            inside_vel = numpy.round(inside_vel, 2)
            outside_vel = numpy.round(outside_vel, 2)

            if (dir == 'F'):
                return ("( " + str(Turtlebot_rpm_gen(inside_vel)) + ", " + str(Turtlebot_rpm_gen(outside_vel)) + ")")
            if (dir == 'R'):
                return ("( " + str((-1)*Turtlebot_rpm_gen(inside_vel)) + ", " + str((-1)*Turtlebot_rpm_gen(outside_vel)) + ")")
            else:
                print("invalid direction")
                return ("( " + str(0) + ", " + str(0) + ")")
        else: #inside wheels
            ICC = abs(ICC)
            omega = vel / ICC
            inside_vel = omega * ((CTC / 2) - ICC)
            outside_vel = omega * ((CTC / 2) + ICC)
            inside_vel = numpy.round(inside_vel, 2)
            outside_vel = numpy.round(outside_vel, 2)

            if (dir == 'F'):
                return ("( " + str((-1)*Turtlebot_rpm_gen(inside_vel)) + ", " + str(Turtlebot_rpm_gen(outside_vel)) + ")")
            if (dir == 'R'):
                return ("( " + str(Turtlebot_rpm_gen(inside_vel)) + ", " + str((-1)*Turtlebot_rpm_gen(outside_vel)) + ")")
            else:
                print("invalid direction")
                return ("( " + str(0) + ", " + str(0) + ")")



max_vel = .22  # m/s
x = 0
while (x != 'q'):
    print("")
    print("Exit with 'q'")
    print("Enter Turtlebot velocity:")
    x = raw_input()

    if (x == 'q'):
        continue

    try:
        val = float(x)
        if (val > max_vel):
            print("Invalid Velocity Request!")
            continue
    except ValueError:
        print("That's not a valid float.")


    print("Enter Turtlebot Direction:")
    dir = raw_input()

    print("Enter Turtlebot ICC:")
    ICC = raw_input()

    try:
        ICC = float(ICC)
        print(p5_control(val,dir,ICC))


    except ValueError:
        print("Using None for ICC.")
        print(p5_control(val, dir))



