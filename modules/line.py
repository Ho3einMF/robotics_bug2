from config import destination

def get_slope(first_point, second_point):
    # x2 = second_point[0], y2 = second_point[1]
    # x1 = first_point[0], y1 = first_point[1]
    # formula ⟹ m = (y2 - y1) / (x2 - x1) 
    return (second_point[1] - first_point[1]) / (second_point[0] - first_point[0])

def is_robot_on_the_line(x, y, slope):
    # y - y1 = m (x - x1)
    # destination vector (target position) ⟹ (x1, y1)

    x1 = destination[0]
    y1 = destination[1]
    m = slope

    print('m : ', m)
    print(f'x : {x} , y : {y}')
    print(f'x1 : {x1} , y1 : {y1}')
    
    diff_equation = abs((y - y1) - m * (x - x1))
    print('diff equation : ', diff_equation)

    if diff_equation < 0.05:
        return True
    return False