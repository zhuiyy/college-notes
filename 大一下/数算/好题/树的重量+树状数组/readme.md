# [树状数组的基本操作](https://blog.csdn.net/TheWayForDream/article/details/118436732#)    
    
    
    def BITlowbit(x):
            return x & (-x)

    def BITadd(x, a):
        global B
        i = xx
        while i <= 某个上限:
            B[i] += a
            i += BITlowbit(i)

    def BITprefix(x):
        global B
        i = x
        ans = 0
        while i > 0:
            ans += B[i]
            i -= BITlowbit(i)
        return ans

    def BITquery(a, b):
        return BITprefix(b) - BITprefix(a - 1)

实现一个列表的插入O(log(n)), 查询片段和O(log(n))