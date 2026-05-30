class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1
        while l<=r:
            if nums[l] < nums[r]:
                return min(nums[l], res)
            mid = (l+r)//2
            if nums[mid] >= res:
                l = mid + 1
            else:
                res = nums[mid]
                r = mid-1
        return res
        
