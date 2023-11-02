# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/?envType=daily-question&envId=2023-11-02

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CountNodesEqualToAverageOfSubtree_2265:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def calculate(node: Optional[TreeNode]):
            nonlocal res
            if not node:
                return (0, 0)
            left = calculate(node.left)
            right = calculate(node.right)

            cnt = 1 + left[0] + right[0]
            total_sum = node.val + left[1] + right[1]
            avg = total_sum // cnt

            res += 1 if avg == node.val else 0
            return (cnt, total_sum)
        calculate(root)
        return res
