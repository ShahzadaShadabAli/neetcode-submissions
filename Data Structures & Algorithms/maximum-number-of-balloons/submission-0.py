class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        fixed = {"b":1, "l":2, "o":2,"n":1, "a":1}
        res = 0
        count = Counter(text)
        while True:
            if count["b"]>=fixed["b"] and count["a"]>=fixed["a"] and count["l"]>=fixed["l"] and count["n"]>=fixed["n"] and count["o"]>=fixed["o"]:
                res+=1
                count["b"] -= fixed["b"]
                count["a"] -= fixed["a"]
                count["l"] -= fixed["l"]
                count["o"] -= fixed["o"]
                count["n"] -= fixed["n"]
            else:
                return res