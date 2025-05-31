from collections import deque as q

s = int(input())
actions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(s):
    [n, m] = list(map(int, input().split()))
    mapp = []
    flag_start  = 0
    start = None
    for i in range(n):
        k = input().strip()
        mapp.append(k)
        if not flag_start:
            for j in range(m):
                if k[j] == 'r':
                    start = (i, j, True)
                    flag_start = 1
                    break
    olist = q([start])
    cl = [[-1 for i in range(m)] for i in range(n)]
    cl[start[0]][start[1]] = 0
    ans = None
    while olist:
        current = olist.pop()
        if current[2] == False:
            olist.appendleft((current[0], current[1], True))
            continue
        for i in actions:
            newi = current[0] + i[0]
            newj = current[1] + i[1]
            if 0 <= newi <= n - 1 and 0 <= newj <= m - 1:
                if cl[newi][newj] == -1:
                    if mapp[newi][newj] == '#':
                        cl[newi][newj] = None
                    elif mapp[newi][newj] == 'x':
                        cl[newi][newj] = cl[current[0]][current[1]] + 2
                        olist.appendleft((newi, newj, False))
                    elif mapp[newi][newj] == '@':
                        cl[newi][newj] = cl[current[0]][current[1]] + 1
                        olist.appendleft((newi, newj, True))
                    else:
                        ans = cl[current[0]][current[1]] + 1
                        flag = 1
                        break
        if ans != None:
            print(ans)
            break
    else:
        print('Impossible')