import math

[k, n] = list(map(int, input().split()))

contribute = [0 for i in range(2 ** k)]
pre_ord_key = [0 for i in range(2 ** k)]
size = [0] + [2 ** (k - int(math.log2(i))) - 1 for i in range(1, 2 ** k)]
B = [0 for i in range(2 ** k)]
key = 1

def pre_order(a):
    global pre_ord_key, key
    if a > 2 ** k - 1:
        return
    pre_ord_key[a] = key
    key += 1
    pre_order(a * 2)
    pre_order(a * 2 + 1)

pre_order(1)
def BITlowbit(x):
        return x & (-x)

def BITadd(x, a):
    global k, B, pre_ord_key
    i = pre_ord_key[x]
    while i <= 2 ** k - 1:
        B[i] += a
        i += BITlowbit(i)

def BITprefix(x):
    i = x
    ans = 0
    global B
    while i > 0:
        ans += B[i]
        i -= BITlowbit(i)
    return ans

def BITquery(a, b):
    return BITprefix(b) - BITprefix(a - 1)

for _ in range(n):
    l = list(map(int, input().split(' ')))
    if l[0] == 1:
        BITadd(l[1], l[2] * size[l[1]])
        contribute[l[1]] += l[2] * size[l[1]]
    else:
        an = BITquery(pre_ord_key[l[1]], pre_ord_key[l[1]] + size[l[1]] - 1)
        i = l[1]
        while i != 1:
            i //= 2
            an += contribute[i] // size[i] * size[l[1]]
        print(an)