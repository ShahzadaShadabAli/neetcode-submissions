class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            target = -nums[i]
            while l<r:

                    
                find = nums[l]+nums[r]
                if find < target:
                    l+=1
                elif find > target:
                    r-=1
                else:
                    print(i, l, r)
                    res = [nums[i], nums[l], nums[r]]
                    if res not in output:
                        output.append(res)
                    l+=1
        return output
                
