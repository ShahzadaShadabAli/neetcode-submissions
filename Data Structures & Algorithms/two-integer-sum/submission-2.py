class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two = {}
        # for i in range(len(nums)):
        #     diff = (target-nums[i])
        #     if diff in two:
        #         return [two[diff], i]
        #     else:
        #         two[nums[i]] = i

        diffSet = {}
        for i, n in enumerate(nums):
            diff = target-n
            if diff in diffSet:
                return [diffSet[diff], i]
            else:
                diffSet[n] = i