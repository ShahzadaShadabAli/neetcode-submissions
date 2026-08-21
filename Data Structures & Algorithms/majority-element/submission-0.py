class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        for n in nums:
            hashMap[n]= 1+hashMap.get(n, 0)
            if hashMap[n] > int(len(nums)/2):
                return n