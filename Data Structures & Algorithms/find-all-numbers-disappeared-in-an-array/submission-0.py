class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        maxi = len(nums)+1
        nums = set(nums)
        res =[]
        for i in range(1,maxi):
            print(i)
            if i not in nums:
                res.append(i)
        return res