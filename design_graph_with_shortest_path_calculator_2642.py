# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/submissions/1096481801/?envType=daily-question&envId=2023-11-11

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = []
        for i in range(n):
            self.graph.append([])
        
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        n = len(self.graph)
        costs = [int(1e+9)] * n
        costs[node1] = 0
        pq = [(0, node1)]

        while pq:
            cur_cost, cur_node = heappop(pq)
            if cur_cost > costs[cur_node]:
                continue
            if cur_node == node2:
                return cur_cost
            for nxt_node, nxt_cost in self.graph[cur_node]:
                new_cost = cur_cost + nxt_cost

                if new_cost < costs[nxt_node]:
                    costs[nxt_node] = new_cost
                    heappush(pq, (new_cost, nxt_node))
        return -1;


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
