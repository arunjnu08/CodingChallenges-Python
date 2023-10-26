# https://leetcode.com/problems/binary-trees-with-factors/?envType=daily-question&envId=2023-10-26 

class BinaryTreesWithFactors823:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        mod = int(1e+9 + 7)

        dp = {}
        for x in arr:
            dp[x] = 1
        
        for i in range(1, n):
            for j in range(i):
                x = arr[j]
                y = arr[i] // arr[j]
                if y < x:
                    break;
                if arr[i] % arr[j] == 0 and y in dp:
                    dp[arr[i]] = (dp[arr[i]] + (1 if x == y else 2) * dp[x] * dp[y]) % mod
        
        res = 0
        for x in arr:
            res += dp[x]
        return res % mod
        
