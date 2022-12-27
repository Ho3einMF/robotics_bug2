import math

from config import destination

def get_distance_to_target(gps):
    current_position = get_current_position(gps)
    return math.sqrt((destination[0] - current_position[0]) ** 2 + (destination[1] - current_position[1]) ** 2)

def get_current_position(gps):
    current_position = gps.getValues()
    x = current_position[0]
    y = current_position[1]
    return (x, y)