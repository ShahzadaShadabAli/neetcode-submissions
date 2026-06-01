class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        long = 1
        if len(s) == 0:
            return 0
        for right in range(1, len(s)):
            print(s[right], s[left:right])
            if s[right] in s[left:right]:
                while s[right] in s[left:right]:
                    left+=1
            else:
                long = max(long, len(s[left:right+1]))
        return long