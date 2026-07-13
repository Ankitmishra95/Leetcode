# 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def fun(i,n):
            if i == n:
                return 1
            if i > n:
                return 0

            if i in dp:
                return dp[i]
            
            ans = fun(i+1,n) + fun(i+2,n)

            dp[i] = ans

            return ans
        return fun(0,n)