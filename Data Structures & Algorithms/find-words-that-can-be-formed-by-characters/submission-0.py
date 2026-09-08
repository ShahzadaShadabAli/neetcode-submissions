class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res=0
        charCount = Counter(chars)
        for w in words:
            flag = True
            count = Counter(w)
            for i in count:
                if count[i]>charCount[i]:
                    flag=False
            if flag:
                res+=len(w)
                    
        return res