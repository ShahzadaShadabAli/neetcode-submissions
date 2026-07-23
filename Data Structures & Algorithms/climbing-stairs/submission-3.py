class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = {}
        # def check(n):
        #     if memo.get(n, False): return memo[n]
        #     if n == 1:
        #         return 1
        #     if n == 2:
        #         return 2
        #     res = check(n-1)+check(n-2)
        #     memo[n] = res
        #     return res
        # return check(n)
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one+=two
            two=temp
        return one




























