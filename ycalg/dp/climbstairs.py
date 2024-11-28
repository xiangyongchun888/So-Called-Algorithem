"""
Condition: You are climbing a stair case. It takes n steps to reach to the top.
Update: Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Goal: Return the number of distinct ways to reach the top.
Author: Yongchun
Date: 2024-11-28
"""

# Solution 1: Brute Force
class solution1:
    def ClimbStairs(self, n: int) -> int:
        return self.climb_stairs(0, n)
    
    def climb_stairs(self,i:int, n: int) -> int:
        if i > n:
            return 0
        if i == n:
            return 1
        return self.climb_stairs(i + 1, n) + self.climb_stairs(i + 2, n)
    