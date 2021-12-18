import heapq as hq
from typing import NoReturn

data = ''''''

# ALWAYS Y, X
def up(coords):
    return (coords[0]-1, coords[1])

def down(coords):
    return (coords[0]+1, coords[1])

def left(coords):
    return (coords[0], coords[1]-1)

def right(coords):
    return (coords[0], coords[1]+1)


moves = [
    lambda x: up(x),
    lambda x: down(x),
    lambda x: left(x),
    lambda x: right(x),
]


def get_neighbours(coords):
    neigh = {}
    for move in moves:
        neighbour_coords = move(coords)
        try:
            if neighbour_coords[0] < 0 or neighbour_coords[1] < 0:
                continue
            neigh[neighbour_coords] = adjacency[neighbour_coords[0]][neighbour_coords[1]]
        except IndexError:
            continue
    return neigh

def get_point(point, coll):
    for elem in coll:
        if elem.point[0] == point[0] and elem.point[1] == point[1]:
            return elem
    return None

def update_dist(point, new_cost):
    for elem in costs:
        if elem.point[0] == point[0] and elem.point[1] == point[1]:
            elem.cost = new_cost
        
class Element:
    def __init__(self, point, start, cost):
        self.point = point
        self.start = start
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost
    



adjacency = []
lines = [line for line in data.split("\n") if line]
for y_index, line in enumerate(lines):
    adjacency.append([0] * len(lines[0]))
    costs = list(line)
    for x_index in range(len(costs)):
        adjacency[y_index][x_index] = int(costs[x_index])


start = Element((0, 0),None,0)
queue = [Element(neigh,start.point, 0) for neigh in get_neighbours(start.point)]
hq.heapify(queue)
costs = [start]
visited = []


while len(queue) > 0:
    # Get the current node from queue
    neigh = hq.heappop(queue)

    if get_point(neigh.point, visited) is None:
        visited.append(Element(neigh.point, -1, -1))

        # Same point as neigh but e.g. reached from a different start 
        prev_point = get_point(neigh.point, costs)

        # previous cost + current cost
        current_cost = (neigh.cost + adjacency[neigh.point[0]][neigh.point[1]])

        if prev_point is None:
            costs.append(Element(
                neigh.point,
                neigh.start,
                current_cost
            ))
        else:
            if prev_point.cost > current_cost:
                update_dist(neigh.point, current_cost)

        if neigh.point != ((len(adjacency)-1), (len(adjacency)-1)):
            # Add neighbours to queue
            neighs = [Element(new_neigh,neigh.point,current_cost) for new_neigh in get_neighbours(neigh.point)]
            for new_neigh in neighs:
                new_neigh_point = new_neigh.point
                if get_point(new_neigh_point, costs) is not None:
                    if (current_cost + adjacency[new_neigh_point[0]][new_neigh_point[1]]) < get_point(new_neigh_point, costs).cost:
                        hq.heappush(queue, new_neigh)
                else:
                    hq.heappush(queue, new_neigh)


final = get_point((99,99), costs)
print(f"Solution: {final.cost}")