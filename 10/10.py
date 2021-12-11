stop_chars = {
    "(":")",
    "[":"]",
    "{":"}",
    "<":">",
}

input = '''
'''

def jump_chunk(stop_char, line, jump):
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
            res = jump_chunk(stop_chars[char], line, jump)
            if type(res) is int:
                # Valid chunk found
                # => Jump over valid chunk to continue current chunk
                jump = res
                return jump_chunk(stop_char, line, jump)
            else:
                # Corrupted char found => return
                return res
    return jump



parsed = [list(line) for line in input.split("\n") if line]
err = 0
for line in parsed:
    print(line)
    test = jump_chunk(stop_chars[line[0]], line, 0)
    if type(test) is str:
        print(f"==> INVALID -> {test}\n")
        if test == ")":
            err += 3
        if test == "]":
            err += 57
        if test == "}":
            err += 1197
        if test == ">":
            err += 25137

    else:
        print("==> VALID\n")   
        continue


print(f"Solution: {err}")
