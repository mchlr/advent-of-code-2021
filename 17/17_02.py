import copy
from tqdm import tqdm

x_max = 1
x_min= 1

y_max = -1
y_min = -1

def is_in_area(coords):
    return (coords[0] >= x_min and coords[0] <= x_max) and (coords[1] >= y_min and coords[1] <= y_max) 

def has_overshot(coords):
    if coords[0] > x_max:
        return True
    if coords[1] < y_min:
        return True
    return False

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
    vel = copy.copy(velocity)
    pos = copy.copy(position) 
    while True:
        vel, pos = do_step(copy.copy(vel), copy.copy(pos))

        y_values.append(pos[1])

        if is_in_area(pos):
            return max(y_values)
        if has_overshot(pos):
            return -3.141592654


# Grid search all trajectory
possible_velo = []

for i in tqdm(range(-200, 200, 1)):
    for j in range(-200, 200, 1):
        y = shoot([i,j], [0,0])

        if y != -3.141592654:        
            possible_velo.append([i,j])

print(f"Solution: {len(possible_velo)}")