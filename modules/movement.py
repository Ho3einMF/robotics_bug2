from config import max_speed

def smart_rotation(robot_angle, target_angle):
    right_rotation_to_target_angle = (360 - robot_angle) + target_angle
    if right_rotation_to_target_angle > 360:
        right_rotation_to_target_angle = right_rotation_to_target_angle - 360
    left_rotation_to_target_angle = 360 - right_rotation_to_target_angle

    if right_rotation_to_target_angle <= left_rotation_to_target_angle:
        right_speed = -1
        left_speed = 1
        print('turn right')
    else:
        right_speed = 1
        left_speed = -1
        print('turn left')

    return left_speed, right_speed

def wall_follower(proximity_sensors):
    # wall following algorithm
            front_wall = proximity_sensors[0].getValue() > 80 or proximity_sensors[7].getValue() > 80
            left_wall = proximity_sensors[5].getValue() > 80
            too_close_left = proximity_sensors[6].getValue() > 80
            right_wall = proximity_sensors[1].getValue() > 80
            too_close_right = proximity_sensors[2].getValue() > 80

            print('front_wall : ', front_wall)
            print('left_wall : ', left_wall)
            print('too_close_left : ', too_close_left)

            if right_wall or too_close_right:
                right_speed = -1
                left_speed = 1

            elif front_wall:
                print('Turn right')
                right_speed = -1
                left_speed = 1

            else:
                if left_wall:
                    print('Drive forward')
                    right_speed = max_speed
                    left_speed = max_speed

                else:
                    print('Turn left')
                    right_speed = max_speed
                    left_speed = max_speed / 4

                if too_close_left:
                    print('Too close left')
                    right_speed = -1
                    left_speed = 1

            return right_speed, left_speed