'''
https://leetcode.com/problems/validate-binary-tree-nodes/?envType=daily-question&envId=2023-10-17
'''
class ValidateBinaryTreeNodes:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        par = [None] * n
        for i in range(n):
            if leftChild[i] != -1:
                if not par[leftChild[i]]:
                    par[leftChild[i]] = i
                else:
                    return False
            
            if rightChild[i] != -1:
                if not par[rightChild[i]]:
                    par[rightChild[i]] = i
                else:
                    return False
        # print(par)
        
        root = None
        for i in range(n):
            if par[i] is None:
                if root is None:
                    root = i
                else:
                    # print(f"par[{i}] = {par[i]}  root = {root}")
                    return False
        
        if root is None:
            return False
        # print(f"root = {root}")
        
        q = []
        vis = [False] * n
        q.append(root)
        vis[root] = True

        while len(q):
            node = q.pop(0)
            left = leftChild[node]
            right = rightChild[node]

            if left != -1:
                if vis[left]:
                    return False
                q.append(left)
                vis[left] = True
            
            if right != -1:
                if vis[right]:
                    return False
                q.append(right)
                vis[right] = True
        
        for ele in vis:
            if not ele:
                return False
        return True
