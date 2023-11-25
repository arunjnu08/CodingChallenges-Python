# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description/?envType=daily-question&envId=2023-11-25

class SumOfAbsoluteDifferencesInASortedArray_1685:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, sum(nums)
        ans = [0] * n
        for i in range(n):
            ans[i] = (nums[i] * i - left) + (right - nums[i] * (n - i))
            left += nums[i]
            right -= nums[i]
        return ans
