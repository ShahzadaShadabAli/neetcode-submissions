class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        ransom = {}
        for c in ransomNote:
            ransom[c]=1+ransom.get(c, 0)
            if ransom[c] > count.get(c, 0):
                return False
        return True