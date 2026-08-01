class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        path = []

        digitToLetter = {"2":"abc", "3": "def", "4":"ghi", "5": "jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        def dfs(i, word):
            if len(word) == len(digits):
                res.append(word)
                return
            
            if i == len(digits):
                return

            for letter in digitToLetter[digits[i]]:
                dfs(i+1, word+letter)
        
        if digits:
            dfs(0, "")
        return res