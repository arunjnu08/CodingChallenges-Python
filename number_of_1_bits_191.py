# https://leetcode.com/problems/number-of-1-bits/description/?envType=daily-question&envId=2023-11-29

class NumberOf_1_Bits:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n != 0:
            cnt += 1
            n = (n & (n - 1))
        return cnt
