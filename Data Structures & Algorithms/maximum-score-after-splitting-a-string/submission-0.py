class Solution:
    def maxScore(self, s: str) -> int:
        result = 0
        for i in range(1, len(s)):
            res=0
            for n in (s[:i]):
                if n=="0":
                    res+=1
            for k in s[i:]:
                res+=int(k)
            result = max(result, res)
        return result