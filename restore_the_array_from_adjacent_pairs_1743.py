# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/submissions/1095703202/?envType=daily-question&envId=2023-11-10

class RestoreTheArrayFromAdjacentPairs_1743:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs) + 1
        graph = {}
        for u, v in adjacentPairs:
            if not u in graph:
                graph[u] = []
            if not v in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        
        res = []
        ele = 0
        for u in graph:
            if len(graph[u]) == 1:
                ele = u
                break
        
        pre = ele
        while len(res) < n:
            res.append(ele)
            for nxt in graph[ele]:
                if nxt != pre:
                    pre = ele
                    ele = nxt
                    break
        return res
