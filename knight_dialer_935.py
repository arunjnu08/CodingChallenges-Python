# https://leetcode.com/problems/knight-dialer/description/?envType=daily-question&envId=2023-11-27

class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1: return 10
        dp = [1] * 10
        jumps = (
            (4, 6),
            (6, 8),
            (7, 9),
            (4, 8),
            (0, 3, 9),
            (),
            (0, 1, 7),
            (2, 6),
            (1, 3),
            (2, 4)
        )
        mod = 1000000007

        for i in range(2, n + 1):
            dp1 = [0] * 10
            for j in range(10):
                for num in jumps[j]:
                    dp1[j] = (dp1[j] + dp[num]) % mod
            dp = dp1
        return sum(dp) % mod
