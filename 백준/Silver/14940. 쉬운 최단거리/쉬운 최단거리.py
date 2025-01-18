import sys
from collections import deque

input = sys.stdin.readline

def setting():
    row, col = len(maps), len(maps[0])
    array = [[-1] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if maps[i][j] == 2:
                array[i][j] = 0
                target = (i, j)

            elif maps[i][j] == 0:
                array[i][j] = 0
    return target, array

def solve(i, j):
    waiting = deque([(i, j)])

    while waiting:
        r, c = waiting.popleft()

        for d in directions:
            x, y = r + d[0], c + d[1]

            if x < 0 or x >= n or y <0 or y >= m:
                continue

            if result[x][y] > -1:
                continue

            result[x][y] = result[r][c] + 1
            waiting.append((x, y))


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

pos, result = setting()
solve(pos[0], pos[1])

for r in result:
    print(' '.join(list(map(str, r))))