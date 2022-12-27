def initialize_motors(robot):
    right_motor = robot.getDevice('right wheel motor')
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0)

    left_motor = robot.getDevice('left wheel motor')
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0)

    return right_motor, left_motor

def initialize_compass(robot, timestep):
    compass = robot.getDevice('compass')
    compass.enable(timestep)
    return compass

def initialize_gps(robot, timestep):
    gps = robot.getDevice('gps')
    gps.enable(timestep)
    return gps

def initialize_proximity_sensors(robot, timestep):
    proximity_sensors = []
    for i in range(8):
        proximity_sensors.append(robot.getDevice(f'ps{i}'))
        proximity_sensors[i].enable(timestep)
    return proximity_sensors