import heapq
n = int(input())
h = list(map(int, input().split()))
heapq.heapify(h)
ans = 0
for _ in range(n - 1):
    k = 0
    for u in range(2):
        k += heapq.heappop(h)
    heapq.heappush(h, k)
    ans += k
print(ans)