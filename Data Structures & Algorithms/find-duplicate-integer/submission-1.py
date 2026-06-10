class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sets = set()
        for i,n in enumerate(nums):
            if n in sets:
                return n
            else:
                sets.add(n)