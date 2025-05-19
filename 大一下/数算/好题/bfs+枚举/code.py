from collections import deque as q
import sys

l = []
island = []
n = int(sys.stdin.readline())

for _ in range(n):
    line = sys.stdin.readline().strip()
    l.append(list(line))

actions = ((-1, 0), (1, 0), (0, -1), (0, 1))

def bfs(a, b):
    global l
    c_island = []
    ol = q()
    ol.append((a, b))
    while len(ol):
        a, b = ol.popleft()
        c_island.append((a, b))
        for i, j in actions:
            if 0 <= a + i < n and 0 <= b + j < n and l[a + i][b + j] == '1':
                ol.append((a + i, b + j))
                l[a + i][b + j] = '0'
    return c_island

for i in range(n):
    for j in range(n):
        if l[i][j] == '1':
            island.append(bfs(i, j))

min = 2 * n
for (x1, y1) in island[0]:
    for (x2, y2) in island[1]:
        k = abs(x1 - x2) + abs(y1 - y2)
        if k < min:
            min = k

print(min - 1)
