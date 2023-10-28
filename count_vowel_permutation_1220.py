# https://leetcode.com/problems/count-vowels-permutation/?envType=daily-question&envId=2023-10-28 

class CountVowelPermutation1220:
    def countVowelPermutation(self, n: int) -> int:
        dp1 = [1] * 5
        res = 5
        mod = int(1e+9 + 7)

        for i in range(2, n + 1):
            dp2 = [0] * 5
            dp2[0] = dp1[1] % mod
            dp2[1] = (dp1[0] + dp1[2]) % mod
            dp2[2] = (sum(dp1) - dp1[2]) % mod
            dp2[3] = (dp1[2] + dp1[4]) % mod
            dp2[4] = dp1[0] % mod
            res = sum(dp2) % mod
            dp1 = dp2
        return res
