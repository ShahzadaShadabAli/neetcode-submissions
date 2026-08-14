class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # Take the shortest string as the baseline candidate
        shortest = min(strs, key=len)

        for i, char in enumerate(shortest):
            for s in strs:
                # If any string does not match the character at position i
                if s[i] != char:
                    return shortest[:i]

        return shortest