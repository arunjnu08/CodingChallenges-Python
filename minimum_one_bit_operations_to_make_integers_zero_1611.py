# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/?envType=daily-question&envId=2023-11-30

class MinimumOneBitOperationsToMakeIntegersZero_1611:
    def minimumOneBitOperations(self, n: int) -> int:
        ans, cnt = 0, 0
        while n > 0:
            cnt += 1
            if (n & 1) == 1:
                ans = (1 << cnt) - 1 - ans
            n = (n >> 1)
        return ans
