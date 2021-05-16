# 1304. 和为零的N个唯一整数 easy
class Solution:
    def sumZero(self, n: int) -> List[int]:
        l = []
        for i in range(n-1):
            if n % 2 == 1 and i == 0:
                l.append(0)
            elif(i%2==1):
                l.append(i)
            elif(i%2==0):
                l.append(-(i+1))
        l.append(-(sum(l)))
        # l.sort()
        l = sorted(l)
        return l
