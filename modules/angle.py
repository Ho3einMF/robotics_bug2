import math

from location import get_current_position
from config import start_point, destination

def get_head_in_degrees(compass):
    head = math.degrees(math.atan2(compass[1], compass[0]))
    if (head < 0.0):
        head = head + 360
    return head

def get_rigth_in_degrees(compass):
    head = get_head_in_degrees(compass)
    # plus 3 for fix measurement error
    right = head + 90
    if right > 360:
        right = abs(360 - right)
    return right

def get_quadrant(x, y, gps):
    # Transfer the origin of the coordinates to the initial coordinates of the robot to get quadrant relative to the robot
    
    current_position = get_current_position(gps)
    x = x - current_position[0]
    y = y - current_position[1]

    print('x in quarant : ', x)
    print('y in quarant : ', y)

    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return None

def get_direction(x, y):
    # Transfer the origin of the coordinates to the initial coordinates of the robot to get quadrant relative to the robot
    x = x - start_point[0]
    y = y - start_point[1]

    if x == 0:
        if y > 0:
            return 'up'
        else:
            return 'down'
    elif y == 0:
        if x > 0:
            return 'right'
        else:
            return 'left'

def get_target_angle(gps):
    # CosΘ = a.b / |a| * |b| ⟹ Θ = ArcCos (a.b / |a| * |b|)

    # unit vector align north direction (J)
    robot_to_north_vector = (0, 1)

    current_position = get_current_position(gps)
    robot_to_target_vector = (destination[0] - current_position[0], destination[1] - current_position[1])

    a_dot_b = robot_to_north_vector[0] * robot_to_target_vector[0] + robot_to_north_vector[1] * robot_to_target_vector[1]
    a_length = math.sqrt(robot_to_north_vector[0] ** 2 + robot_to_north_vector[1] ** 2)
    b_length = math.sqrt(robot_to_target_vector[0] ** 2 + robot_to_target_vector[1] ** 2)

    angle = math.degrees(math.acos(a_dot_b / (a_length * b_length)))

    quadrant = get_quadrant(x=destination[0], y=destination[1], gps=gps)
    print('quadrant : ', quadrant)
    if quadrant:
        if quadrant == 2 or quadrant == 3:
            angle = 360 - angle
    
    else:
        direction = get_direction(x=destination[0], y=destination[1])
        print('direction : ', direction)
        if direction == 'left':
            angle = 270

    return angle