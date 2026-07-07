class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {"]":"[", "}":"{", ")":"("}

        for ch in s:
            # If we encounter a closing bracket
            if ch in valid:
                # No matching opening bracket
                if not stack:
                    return False
                # No matching opening bracket in sequence
                if valid[ch] != stack.pop():
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0


     
