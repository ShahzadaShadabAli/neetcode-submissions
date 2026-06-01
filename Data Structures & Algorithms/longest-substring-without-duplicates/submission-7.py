class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, long = 0, 1
        if len(s) == 0:
            return 0
        for right in range(1, len(s)):
            while s[right] in s[left:right]:
                left+=1
            long = max(long, len(s[left:right+1]))
        return long