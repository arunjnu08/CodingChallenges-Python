"""
https://leetcode.com/problems/constrained-subsequence-sum/?envType=daily-question&envId=2023-10-21 
"""

class ConstrainedSubsequenceSum:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dq = deque()
        n = len(nums)

        dq.appendleft((nums[n - 1], n - 1))
        res = nums[n - 1]

        for i in range(n - 2, -1, -1):
            while(dq[-1][1] - i > k):
                dq.pop()
            
            val = nums[i] + max(0, dq[-1][0])

            while(len(dq) > 0 and val > dq[0][0]):
                dq.popleft()
            
            dq.appendleft((val, i))
            res = max(res, val)
        return res
