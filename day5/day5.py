import re
from copy import deepcopy  # needed to keep track of changes

lines = [line.rstrip() for line in open('input.txt')]
# An empty line separates the crates from the instructions
separator = lines.index('')
# this row shows the amount of columns
numCrates = len(lines[separator-1].split())

crates = [[] for _ in range(numCrates)]
# collect the crates
for line in lines[:separator-1]:
    for j in range(1, len(line), 4):  # a crate is 4 characters
        if line[j] != " ":
            crates[j//4].append(line[j])
for c in crates:
    c.reverse()
    print(c)

moves = [tuple(map(int, re.findall("\d+", move)))
         for move in lines[separator+1:]]

copy1, copy2 = deepcopy(crates), deepcopy(crates)
for num, src, dest in moves:
    for _ in range(num):
        copy1[dest-1].append(copy1[src - 1].pop())
    copy2[dest - 1] += copy2[src - 1][-num:]
    copy2[src - 1] = copy2[src-1][:-num]

print(f"{''.join([crateStack[-1] for crateStack in copy1])}")
print("######################")
print(f"{''.join([crateStack[-1] for crateStack in copy2])}")