input = '''
'''

def calc_sol():
    letter_count = {}
    for letter in letters:
        letter_count[letter] = 0
        for pair in polymer.keys():
            if letter in pair:
                letter_count[letter] += polymer[pair] * pair.count(letter)

    for letter in letter_count.keys():
        letter_count[letter] = round((letter_count[letter] / 2) + 0.001)

    most_common = (letter_count[max(letter_count, key=letter_count.get)])
    least_common = (letter_count[min(letter_count, key=letter_count.get)])

    return most_common - least_common


lines = [line for line in input.split("\n") if line]

start = lines[0]
del lines[0]

perms = {}
for line in lines:
    key, value = line.split(" -> ")
    perms[key] = value
tmp = perms.keys()
letters = []
for key in tmp:
    letters.extend(list(key))

letters = list(set(letters))


polymer = {}

for i in range(len(start)-1):
    pair = start[i]+start[i+1]
    if pair not in polymer:
        polymer[pair] = 1 
    else:
        polymer[pair] += 1 

for i in range(40):
    new_perms = {}
    for key in polymer.keys():
        if key in perms:
            add = perms[key]
            perm_a = key[0] + add
            value = (1 * polymer[key])

            if perm_a not in new_perms:
                new_perms[perm_a] = value
            else:
                new_perms[perm_a] += value
            
            perm_b = add + key[1]
            if perm_b not in new_perms:
                new_perms[perm_b] = value
            else:
                new_perms[perm_b] += value

    polymer = new_perms      

    # Print solution for part 1
    if (i+1) == 10:      
        print(f"Solution - Part 1: {calc_sol()}")
            
# Print solution for part 2
print(f"Solution - Part 2: {calc_sol()}")