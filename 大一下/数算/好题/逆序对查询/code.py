n = int(input())

def dsort(l):
    if len(l) <= 1:
        return (0, l)
    else:
        mid = len(l) // 2 - 1
        l1 = l[0: mid + 1]
        l2 = l[mid + 1:]
        k1, l1 = dsort(l1)
        k2, l2 = dsort(l2)
        ln = []
        i, j = 0, 0
        kn = 0
        while i <= mid and j < len(l2):
            if l1[i] <= l2[j]:
                ln.append(l1[i])
                i += 1
            else:
                ln.append(l2[j])
                j += 1
                kn += mid - i + 1
        if i > mid:
            ln += l2[j::]
        if j >= len(l2):
            ln += l1[i::]
        return (k1 + k2 + kn, ln)
        

while n != 0:
    l = list(map(int, input().split(' ')))
    print(dsort(l)[0])
    n = int(input())