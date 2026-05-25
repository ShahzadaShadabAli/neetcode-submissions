class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {")":"(", "}":"{", "]":"["}
        for ch in s:
            print(stack)
            if ch in match:
                if not stack:
                    print("dih")
                    return False
                if match[ch] != stack.pop():
                    print("lover")
                    return False
            else:
                stack.append(ch)
        return len(stack)==0
     
