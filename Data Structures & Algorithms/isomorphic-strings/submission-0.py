class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMapT = {}
        hashMapS = {}
        for i in range(len(s)):
            hashMapT[t[i]] = 1+hashMapT.get(t[i], 0)
            hashMapS[s[i]] = 1+hashMapS.get(s[i], 0)
            print(hashMapT.values(), hashMapS.values())
            if list(hashMapT.values()) != list(hashMapS.values()):
                return False
        return True
