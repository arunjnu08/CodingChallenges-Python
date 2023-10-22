"""
https://leetcode.com/problems/maximum-score-of-a-good-subarray/description/?envType=daily-question&envId=2023-10-22
"""

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p1, p2 = k - 1, k + 1
        min_ele = nums[k]
        max_val = nums[k]
        cnt = 1

        while p1 >= 0 or p2 < n:
            if p2 == n:
                min_ele = min(min_ele, nums[p1])
                p1 -= 1
            elif p1 < 0 or nums[p1] < nums[p2]:
                min_ele = min(min_ele, nums[p2])
                p2 += 1
            else:
                min_ele = min(min_ele, nums[p1])
                p1 -= 1
            cnt += 1
            max_val = max(max_val, min_ele * cnt)
        return max_val
