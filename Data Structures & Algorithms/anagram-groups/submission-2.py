class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for n in strs:
            sortstuff = "".join(sorted(n))
            if hashMap.get(sortstuff, 0):
                hashMap[sortstuff].append(n)
            else:
                hashMap[sortstuff] = [n]
        return list(hashMap.values())
