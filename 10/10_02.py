import numpy as np

stop_chars = {
    "(":")",
    "[":"]",
    "{":"}",
    "<":">",
}

input = '''
'''

def calc_score(missing_chars):
    res = 0
    for char in missing_chars:
        res *= 5
        if char == ")":
            res += 1
        if char == "]":
            res += 2
        if char == "}":
            res += 3
        if char == ">":
            res += 4
    return res
        

def jump_chunk(stop_char, line, jump, missings):
    jump += 1

    for i in range(jump,len(line)):
        char = line[i]
        if char in list(stop_chars.values()):
            if char != stop_char:
                # Illegal StopChar found!
                # Return to penalize 
                return char
            else:
                # Chunk valid
                return jump
        else:
            res = jump_chunk(stop_chars[char], line, jump, missings)
            if type(res) is int:
                # Valid chunk found
                # => Jump over valid chunk to continue current chunk
                jump = res
                return jump_chunk(stop_char, line, jump, missings)
            else:
                # Corrupted char found => return
                return res
    # Add missing stop chars 
    lineMissed.append(stop_char)
    return jump



parsed = [list(line) for line in input.split("\n") if line]
err = 0
missing_scores = []
for line in parsed:
    sub_chunks = 0
    lineMissed = []
    result = 0
    while type(result) is int and result < len(line):
        sub_chunks += 1
        result = jump_chunk(stop_chars[line[result+1 if result > 0 else result]], line, result, [])

    # end the suffering
    if sub_chunks > 1:
        lineMissed.pop()


    missing_scores.append(calc_score(lineMissed))


missing_scores = sorted(missing_scores)

print(missing_scores)

print(f"Solution: {missing_scores[int((len(missing_scores)-1) / 2)]}")
