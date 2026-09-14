class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        num = len(words)
        hashMap = {}
        for w in words:
            for n in w:
                hashMap[n]=1+hashMap.get(n, 0)
        for c in hashMap:
            if not hashMap[c]%num==0:
                return False
        return True