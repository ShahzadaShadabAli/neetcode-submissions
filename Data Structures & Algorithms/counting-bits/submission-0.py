class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            n = i
            count = 0
            while n:
                count+=n%2
                n = n>>1
            res.append(count)
        return res
        
