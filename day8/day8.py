import operator
import functools


def isVisible(grid: list[list[int]], row: int, col: int):
    rows = len(grid)
    cols = len(grid[0])
    score = [True, True, True, True]
    steps = 1
    while steps < rows or steps < cols:
        above = row - steps
        below = row + steps
        left = col - steps
        right = col + steps

        # -1 is for edges
        score[0] = score[0] and grid[row][col] > (
            grid[above][col] if above >= 0 else -1)
        score[1] = score[1] and grid[row][col] > (
            grid[below][col] if below <= rows-1 else -1)
        score[2] = score[2] and grid[row][col] > (
            grid[row][left] if left >= 0 else -1)
        score[3] = score[3] and grid[row][col] > (
            grid[row][right] if right <= cols - 1 else -1)

        steps += 1
    return any(score)


def scenicScore(grid: list[list[int]], row: int, col: int):
    rows = len(grid)
    cols = len(grid[0])
    scores = [0, 0, 0, 0]

    above = row - 1
    while above >= 0:
        if grid[above][col] < grid[row][col]:
            scores[0] += 1
            above -= 1
        else:
            scores[0] += 1
            break
    below = row + 1
    while below < rows:
        if grid[below][col] < grid[row][col]:
            scores[1] += 1
            below += 1
        else:
            scores[1] += 1
            break
    left = col - 1
    while left >= 0:
        if grid[row][left] < grid[row][col]:
            scores[2] += 1
            left -= 1
        else:
            scores[2] += 1
            break
    right = col + 1
    while right < cols:
        if grid[row][right] < grid[row][col]:
            scores[3] += 1
            right += 1
        else:
            scores[3] += 1
            break

    return scores[0] * scores[1] * scores[2] * scores[3]


grid = []


with open('input.txt') as f:
    for index, line in enumerate(f):
        grid.append([int(c) for c in line.rstrip()])
print(len(grid))

# grid is constructed
"""
grid = [[3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],]
        """
visible = 0
scores = []
# iterate to find visible
# TODO: how heck up and down
for row, i in enumerate(grid):
    for col, _ in enumerate(i):
        # if isVisible(grid, row, col):
        #visible += 1
        scores.append(scenicScore(grid, row, col))


print(visible)
print(max(scores))
