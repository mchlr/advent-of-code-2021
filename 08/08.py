digits = {
  0: ["a", "b", "c", "e", "f", "g"],
  1: ["c", "f"],
  2: ["a", "c", "d", "e", "g"],
  3: ["a", "c", "d", "f", "g"],
  4: ["b","c","d","f"],
  5: ["a", "b","d","f","g",],
  6: ["a", "b", "d", "e", "f", "g"],
  7: ["a", "c", "f"],
  8: ["a", "b", "c", "d", "e", "f", "g"],
  9: ["a", "b", "c", "d", "f", "g"]
}

input = '''
'''

targets = []
for line in input.split("\n"):
  tmp_split = line.split("|")
  if len(tmp_split) > 1:
    print(tmp_split)
    print(len(tmp_split))
    targets.extend([t.strip() for t in tmp_split[1].split(" ")])
  #ident = tmp_split[0].split(" ")



print("all targets")
print(targets)

matches = 0
for segment in targets:
  if len(segment) > 0:
    is_unique = False
    for digit in digits.keys():
      if len(segment) == len(digits[digit]):
        if is_unique:
          is_unique = False
          break
        is_unique = True

    if is_unique:
      matches += 1


print(matches)