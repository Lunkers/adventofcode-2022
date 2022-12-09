"""
Due to the aforementioned Planck lengths, the rope must be quite short; in fact, the head (H) and tail (T) must always be touching 
(diagonally adjacent and even overlapping both count as touching)

If the head is ever two steps directly up, down, left, or right from the tail, 
the tail must also move one step in that direction so it remains close enough:

Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:

"""
import math

start: tuple = (0, 0)
part1Rope: list[tuple] = [start, start]
part2Rope: list[tuple] = [start] * 10


def move(direction: str, amount: int, knot: tuple) -> tuple:
    if direction == "D":
        return (knot[0] - amount, knot[1])
    elif direction == "U":
        return (knot[0] + amount, knot[1])
    elif direction == "R":
        return (knot[0], knot[1] + amount)
    elif direction == "L":
        return (knot[0], knot[1] - amount)


def isTouching(head: tuple, tail: tuple) -> bool:
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1


def moveTail(distance: tuple, tail: tuple) -> tuple:
    if abs(distance[0]) > 1 and abs(distance[1]) >= 1 or abs(distance[0]) >= 1 and abs(distance[1]) > 1:
        # move diagonally
        return (tail[0] + int(math.copysign(1, distance[0])), tail[1] + int(math.copysign(1, distance[1])))
    elif abs(distance[0]) > 1:
        return (tail[0] + int(math.copysign(1, distance[0])), tail[1])
    elif abs(distance[1]) > 1:
        return (tail[0], tail[1] + int(math.copysign(1, distance[1])))
    else:
        return tail


visited = [start]
with open('input.txt') as f:
    while (line := f.readline().rstrip()):
        direction, amount = line.split(" ")
        for i in range(int(amount)):
            part2Rope[0] = move(direction, 1, part2Rope[0])
            # move tail
            for i in range(1, len(part2Rope)):
                distance = (part2Rope[i-1][0] - part2Rope[i][0],
                            part2Rope[i-1][1] - part2Rope[i][1])
                part2Rope[i] = moveTail(distance, part2Rope[i])
                if i == len(part2Rope) - 1:
                    visited.append(part2Rope[i])


print(len(set(visited)))
