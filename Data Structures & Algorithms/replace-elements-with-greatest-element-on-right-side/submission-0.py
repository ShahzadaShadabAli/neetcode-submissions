class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for r in range(len(arr)-1):
            arr[r] = max(arr[r+1:])
        arr[-1] = -1
        return arr