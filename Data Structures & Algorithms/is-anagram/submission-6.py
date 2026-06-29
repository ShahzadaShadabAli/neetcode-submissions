class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = defaultdict(int)
        second = defaultdict(int)
        for n in s:
            first[ord(n)]+=1
        for k in t:
            second[ord(k)]+=1
        if first == second:
            return True
        return False
