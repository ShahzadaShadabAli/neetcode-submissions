class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        s = s.lower()
        while l < r:
            if not self.checkAlphaNum(s[r]):
                r-=1
                continue
            if not self.checkAlphaNum(s[l]):
                l+=1
                continue
            if s[l] != s[r]:
                return False
            r-=1
            l+=1
        return True

    def checkAlphaNum (self, n):
        
        return ord("A") <= ord(n) <= ord("Z") or ord("a") <= ord(n) <= ord("z") or ord("0") <= ord(n) <= ord("9")
