class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, long = 0, 0
        for right in range(len(s)):
            while s[right] in s[left:right]:
                left+=1
            long = max(long, len(s[left:right+1]))
        return long