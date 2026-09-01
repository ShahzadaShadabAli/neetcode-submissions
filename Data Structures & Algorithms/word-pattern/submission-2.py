class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if sorted(list(Counter(pattern).values()))==sorted(list(Counter(s.split()).values())):
            return True
        return False