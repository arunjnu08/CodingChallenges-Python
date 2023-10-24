# https://leetcode.com/problems/find-largest-value-in-each-tree-row/?envType=daily-question&envId=2023-10-24

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindLargestValueInEachTreeRow515:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        q = deque()
        q.append(root)

        while len(q):
            size = len(q)
            max_val = -(1 << 31)
            for i in range(size):
                node = q.popleft()
                max_val = max(max_val, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(max_val)
        return res
