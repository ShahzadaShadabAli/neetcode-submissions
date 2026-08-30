class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        myHash = {}
        res = []
        i = 0
        for r in grid:
            for c in r:
                i+=1
                myHash[c]=1+myHash.get(c, 0)
                if myHash[c] == 2:
                    res.append(c)
        while i:
            if not myHash.get(i,0):
                res.append(i)
        
            i-=1
        return res

                    