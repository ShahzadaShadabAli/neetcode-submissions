class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        s = s.lower()
        while l <= r:
            print(s[l], s[r])
            if not s[r].isalpha() and not s[r].isdigit():
                r-=1
                continue
            if not s[l].isalpha() and not s[l].isdigit():
                l+=1
                continue
            if s[l] != s[r]:
                return False
            r-=1
            l+=1
        return True