class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashStr = {}
        output = []
        for i in range (len(strs)):
            this = sorted (strs[i])
            this = "".join(this)
            if this in list(hashStr.keys()):
                hashStr[this].append(strs[i])
            else:
                hashStr[this] = [strs[i]]
        return list(hashStr.values())
            
