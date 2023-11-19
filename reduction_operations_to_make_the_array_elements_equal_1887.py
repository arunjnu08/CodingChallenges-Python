# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/?envType=daily-question&envId=2023-11-19

class ReductionOperationsToMakeTheArrayElementsEqual_1887:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans, inx = 0, len(nums) - 1
        ele = nums[inx]
        while inx >= 0:
            if ele == nums[0]:
                break
            if ele != nums[inx]:
                ele = nums[inx];
                ans += len(nums) - inx - 1
            inx -= 1
        return ans
