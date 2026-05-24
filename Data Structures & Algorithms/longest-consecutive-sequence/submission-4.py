class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        seq = 1
        long = 1
        nums = set(nums)
        for n in nums:
            if n-1 not in nums:
                while True:
                    if n+1 in nums:
                        seq += 1
                        n+=1
                    else:
                        if seq > long:
                            long = seq
                        seq=1
                        break
        return long
        