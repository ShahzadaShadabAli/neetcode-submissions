class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longestIncrease = longestDecrease = 1
        currentIncrease = currentDecrease = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                currentIncrease+=1
                longestIncrease = max(longestIncrease, currentIncrease)
                currentDecrease = 1
            elif nums[i] > nums[i+1]:
                currentDecrease+=1
                longestDecrease = max(longestDecrease, currentDecrease)
                currentIncrease = 1
            else:
                currentIncrease = currentDecrease = 1
            print(currentIncrease, currentDecrease)
        return max(longestIncrease, longestDecrease)

            