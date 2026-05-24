class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = 1
        largest_seq = 1
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i]+1 == nums[i+1]:
                seq += 1
            else:
                if seq > largest_seq:
                    largest_seq = seq
                seq = 1
        if seq > largest_seq:
                largest_seq = seq
                seq = 1 
        return largest_seq

        