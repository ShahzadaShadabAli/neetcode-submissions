class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = [0]*26
        s2Count = [0]*26

        for c in s1:
            s1Count[ord(c)-ord("a")] += 1

        l = 0
        for r in range(len(s1), len(s2)+1):
            for c in s2[l:r]:
                s2Count[ord(c)-ord("a")] += 1
            if s2Count == s1Count:
                return True
            l+=1
            s2Count = [0]*26
        return False
