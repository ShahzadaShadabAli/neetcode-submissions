class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sets = defaultdict(int)
        for i,n in enumerate(nums):
            sets[n] += 1
            if sets[n] == 2:
                return n