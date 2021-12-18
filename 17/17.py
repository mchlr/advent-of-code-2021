input = "target area: x=20..30, y=-10..-5"


x_max = 30
x_min= 20

y_max = -5
y_min = -10

def is_in_area(coords):
    return (coords[0] >= x_min and coords[0] <= x_max) and (coords[1] >= y_min and coords[1] <= y_max) 

def has_missed(coords):
    if coords[0] > x_max and coords[1] < y_min:

        return (True, 0)

    return (False, 123)

def do_step(velocity, position):
    position[0] += velocity[0]
    position[1] += velocity[1]

    # Drag
    if velocity[0] > 0:
        velocity[0] -= 1
    elif velocity[0] < 0:
        velocity[0] += 1

    # Gravity
    velocity[1] -= 1

    return velocity, position


def shoot(velocity, position):
    y_values = []
    trajectory = [0,0]
    for _ in range(100):
        velocity, position = do_step(velocity, position)
        trajectory.append(position)

        y_values.append(position[1])

        if is_in_area(position):
            return (True, max(y_values), trajectory)

        else:
            missed, correction = has_missed(position)
            if missed:
                return (False, correction, trajectory)
            else:
                continue








max_y = -999999
not_bigger = 0
velocity = [6,9]

while(True):
    
    has_hit, value, trajectory = shoot(velocity, [0,0])

    if not has_hit:
        velocity[value] -= 1
        continue
    else:
        if value > max_y:
            max_y = value
            not_bigger = 0
        else:
            not_bigger += 1
            if not_bigger > 1000:
                break
        velocity[1] += 1

print(f"Solution: {max_y}")





