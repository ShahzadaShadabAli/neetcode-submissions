class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numberSet = set(numbers)
        # for i, n in enumerate(numbers):
        #     find = target-n
        #     if find in numberSet:
        #         j=i+1
        #         while j < len(numbers):
        #             if numbers[j] == find:
        #                 return[i+1, j+1]
        #             j+=1
        l, r = 0, len(numbers)-1
        while l < r:
            sum = numbers[l]+numbers[r]
            if sum > target:
                r-=1
            elif sum < target:
                l+=1
            else:
                return [l+1, r+1]