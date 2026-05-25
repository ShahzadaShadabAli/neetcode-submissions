class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        myStr = []
        match = {"[":"]", "{":"}", "(":")"}
        for n in s:
            if n not in match.keys():
                if len(myStr) == 0:
                    return False
                if match[myStr.pop()] != n:
                    return False
            else:
                myStr.append(n)
        
        if len(myStr) != 0:
            return False
        return True
     
