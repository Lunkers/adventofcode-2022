
import math

start: tuple = (0, 0)
currentHead = start
currentTail = start
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


visited1 = [start]
visited2 = [start]
with open('input.txt') as f:
    while (line := f.readline().rstrip()):
        direction, amount = line.split(" ")
        for i in range(int(amount)):
            part2Rope[0] = move(direction, 1, part2Rope[0])
            currentHead = move(direction, 1, currentHead)
            # move tail part 1
            distancePart1 = (currentHead[0] - currentTail[0],
                             currentHead[1] - currentTail[1])
            currentTail = moveTail(distancePart1, currentTail)
            visited1.append(currentTail)
            # move tail part 2
            for i in range(1, len(part2Rope)):
                distance = (part2Rope[i-1][0] - part2Rope[i][0],
                            part2Rope[i-1][1] - part2Rope[i][1])
                part2Rope[i] = moveTail(distance, part2Rope[i])
                if i == len(part2Rope) - 1:
                    visited2.append(part2Rope[i])


print(f"part 1: {len(set(visited1))}")
print(f"part 2: {len(set(visited2))}")
