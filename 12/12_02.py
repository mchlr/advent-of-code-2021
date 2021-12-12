input = '''
'''


def get_paths(start):
    if start != "start" or start != "end":
        return [line for line in lines if line[0]==start]
    else:
        return []

def is_valid(path):
    has_visited = {}

    if not check_single_caves(path):
        return False

    for p in path:
        if p not in has_visited:
            has_visited[p] = 1
        else:
            has_visited[p] += 1
            if p == "start" or p == "end":
                return False
    return True

def check_single_caves(path):
    hits = 0
    lower_caves = [x for x in set(path) if x.islower() and (x != "start" and x != "end")]
    for c in lower_caves:
        if path.count(c) == 2:
            hits += 1
            if hits > 1:
                return False
        elif path.count(c) > 2:
            return False
    return True



# parse
lines = [(line.split("-")) for line in input.split("\n") if line]

# get uniques for checking
caves = []
for line in lines:
    caves.append(line[0])
    caves.append(line[1])
caves = list(set(caves))

# paths are bidirectional
reversed_lines = []
for line in lines:
    reversed_lines.append([line[1], line[0]])
lines.extend(reversed_lines)

# get start point
paths = [line for line in lines if line[0]=="start"]


finished_paths = []
all_paths = []

# crank dat
while(True):
    # All paths found
    if len(paths) == 0:
        break

    for p in paths:
        if(p[-1] != "end"):
            adj_paths = get_paths(p[-1])
            for adj in adj_paths:
                all_paths.append([*p[:], adj[1]])
        else:
            finished_paths.append(p)

    valid_paths = []
    # remove illegal from all_paths
    for path in all_paths:
        if is_valid(path):
            valid_paths.append(path)

    paths = valid_paths 
    all_paths = []
    
print(f"Solution: {len(finished_paths)}")