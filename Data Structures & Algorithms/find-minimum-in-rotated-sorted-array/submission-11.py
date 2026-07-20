class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] >= res:
                l=mid+1
            else:
                r=mid-1
                res = nums[mid]
        return res
        
