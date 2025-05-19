from collections import deque as q

class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.next = set()
        self.depth = None

[n, r] = input().split()
n = int(n)
root = Node(r)
tree = {r:root}

for i in range(n - 1):
    [a, b] = input().split()
    if a in tree:
        na = tree[a]
    else:
        na = Node(a)
        tree[a] = na
    if b in tree:
        nb = tree[b]
    else:
        nb = Node(b)
        tree[b] = nb
    na.next.add(nb)
    nb.next.add(na)

olist = [(root, 0, None)]
olist = q(olist)
while olist:
    current, cdepth, parent = olist.pop()
    current.depth = cdepth
    if parent:
        current.parent = parent
    for i in current.next:
        if i.depth == None:
            olist.appendleft((i, cdepth + 1, current))

m = int(input())
for i in range(m):
    [a, b] = [tree[i] for i in input().split()]
    if a.depth < b.depth:
        a, b = b, a
    while a.depth != b.depth:
        a = a.parent
    while a.val != b.val:
        a = a.parent
        b = b.parent
    print(a.val)

