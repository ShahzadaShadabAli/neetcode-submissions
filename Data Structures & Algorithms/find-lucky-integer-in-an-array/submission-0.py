class Solution:
    def findLucky(self, arr: List[int]) -> int:
        myHash = Counter(arr)
        largest = -1

        for i in myHash:
            if myHash[i]==i:
                largest = max(largest,i)
        return largest