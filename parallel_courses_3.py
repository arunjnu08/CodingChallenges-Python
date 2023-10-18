"""
https://leetcode.com/problems/parallel-courses-iii/?envType=daily-question&envId=2023-10-18
"""
class ParallelCourses3:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = {}
        for i in range(1, n + 1):
            graph[i] = []
        
        indegree = [0] * (n + 1)
        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1
        
        queue = []
        maxMonths = [0] * (n + 1)
        for i in range(1, n + 1):
            if indegree[i] == 0:
                queue.append(i)
                maxMonths[i] = time[i - 1]
        
        while len(queue):
            u = queue.pop(0)
            for v in graph[u]:
                maxMonths[v] = max(maxMonths[v], maxMonths[u] + time[v - 1])
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        
        return max(maxMonths)
