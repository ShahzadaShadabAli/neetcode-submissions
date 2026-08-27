class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}

        for s in arr:
            count[s] = 1+count.get(s, 0)

        for s in arr:
            if count[s] == 1:
                k -= 1
                if k == 0:
                    return s

        return ""