# https://leetcode.com/problems/find-mode-in-binary-search-tree/?envType=daily-question&envId=2023-11-01

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindModeInBinarySearchTree_501:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        pre, cnt, max_fre = -1, 0, 0
        res = []

        def dfs(node: Optional[TreeNode]):
            nonlocal pre, cnt, max_fre
            if not node:
                return
            dfs(node.left)
            if cnt == 0:
                cnt = 1
                pre = node.val
            elif pre == node.val:
                cnt += 1
            else:
                if cnt == max_fre:
                    res.append(pre)
                elif cnt > max_fre:
                    max_fre = cnt
                    res.clear()
                    res.append(pre)
                pre = node.val
                cnt = 1
            dfs(node.right)
        
        dfs(root)
        if cnt == max_fre:
            res.append(pre)
        elif cnt > max_fre:
            max_fre = cnt
            res.clear()
            res.append(pre)
        return res
