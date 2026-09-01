class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        print(list(Counter(pattern).values()), sorted(list(Counter(s).values())))
        if sorted(list(Counter(pattern).values()))==sorted(list(Counter(s.split()).values())):
            return True
        return False