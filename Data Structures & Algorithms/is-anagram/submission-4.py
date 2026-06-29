class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = defaultdict(list)
        second = defaultdict(list)
        for n in s:
            first[ord(n)].append(n)
        for k in t:
            second[ord(k)].append(k)
        if first == second:
            return True
        return False
