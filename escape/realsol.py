from collections import deque
import math


def solution(map):
    def bfs(x, y, map):
        g = [[None for i in range(c)] for j in range(r)]
        q = deque([(x, y)])
        g[x][y] = 1
        while q:
            u, v = q.popleft()
            for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                a, b = u + i, v + j
                if 0 <= a < r and 0 <= b < c and g[a][b] is None:
                    g[a][b] = g[u][v] + 1
                    if map[a][b] != 1:
                        q.append((a, b))
        return g

    r = len(map)
    c = len(map[0])

    start_end = bfs(0, 0, map)
    end_start = bfs(r - 1, c - 1, map)
    result = math.inf
    for i in range(r):
        for j in range(c):
            if start_end[i][j] and end_start[i][j]:
                result = min(result, start_end[i][j] + end_start[i][j] - 1)

    return result


print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [
      0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
