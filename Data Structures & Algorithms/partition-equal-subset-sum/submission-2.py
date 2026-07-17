class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False

        dp = set()
        dp.add(0)
        target = (sum(nums)//2)

        for i in range(len(nums)-1, -1, -1):
            DPnew = set()
            for n in dp:
                DPnew.add(n+nums[i])
                DPnew.add(n)
            dp = DPnew
            if target in dp:
                return True
        return True if target in dp else False