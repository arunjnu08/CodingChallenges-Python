"""
https://leetcode.com/problems/power-of-four/description/?envType=daily-question&envId=2023-10-23
"""

class PowerOfFour342:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 0:
            if n == 1:
                return True
            if (n & 3) != 0:
                return False
            n = (n >> 2)
        return False
