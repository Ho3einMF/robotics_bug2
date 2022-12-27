"""bug2_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

from angle import get_head_in_degrees, get_rigth_in_degrees, get_target_angle
from line import get_slope, is_robot_on_the_line
from location import get_current_position, get_distance_to_target
from config import max_speed, destination, start_point, obstacle_detected, cross_obstacle, \
    distance_to_target_threshold
from sensors import initialize_motors, initialize_compass, initialize_gps, initialize_proximity_sensors
from movement import wall_follower, smart_rotation

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

right_motor , left_motor = initialize_motors(robot)
compass = initialize_compass(robot, timestep)
gps = initialize_gps(robot, timestep)
proximity_sensors = initialize_proximity_sensors(robot, timestep)

conf = False
right_speed = max_speed
left_speed = max_speed

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:

    if not conf:
        start_point = get_current_position(gps)
        print('start_point : ', start_point)
        slope = get_slope(start_point, destination)
        conf = True

    distance_to_target = get_distance_to_target(gps)
    print('distance_to_target : ', distance_to_target)
    if distance_to_target < distance_to_target_threshold:
        right_speed = 0
        left_speed = 0
        print('receive to target !!!')

    else:
        target_angle = get_target_angle(gps)
        print('target_angle : ', target_angle)

        head_angle = get_head_in_degrees(compass.getValues())
        print('head_angle : ', head_angle)

        diff_target_head = target_angle - head_angle
        print('diff_target_head', diff_target_head)

        right_angle = get_rigth_in_degrees(compass.getValues())
        print('right_angle : ', right_angle)

        print('cross_obstacle : ', cross_obstacle)
        

        # check the distance sensors for obstacle detected
        for i in range(8):
            if proximity_sensors[i].getValue() > 85:
                obstacle_detected = True
                print(f'ps{i} detected obstacle')
                break

        x, y = get_current_position(gps)
        on_the_line = is_robot_on_the_line(x, y, slope)
        print('on_the_line : ', on_the_line)

        diff_right_target = abs(target_angle - right_angle)
        print('diff_right_target : ', diff_right_target)

        another_side = 300 <= diff_right_target or diff_right_target <= 90
        print('another_side : ', another_side)
        if on_the_line and another_side:
            obstacle_detected = False
            cross_obstacle = True

        if proximity_sensors[0].getValue() > 85 or proximity_sensors[7].getValue() > 85:
            obstacle_detected = True
            cross_obstacle = False

        print('obstacle_detected : ', obstacle_detected)
        if obstacle_detected and not cross_obstacle:
            right_speed, left_speed = wall_follower(proximity_sensors)

        # obstacle_detected == False
        else:
            # if robot in the target direction ⟹ drive forward with max speed
            if -1 < diff_target_head < 1:
                right_speed = max_speed
                left_speed = max_speed
            
            # else ⟹ Turn left until you are in the target direction
            else:
                left_speed, right_speed = smart_rotation(robot_angle=head_angle,
                                                         target_angle=target_angle)

    right_motor.setVelocity(right_speed)
    left_motor.setVelocity(left_speed)

    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    

# Enter here exit cleanup code.
