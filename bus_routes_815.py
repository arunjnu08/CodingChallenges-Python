# https://leetcode.com/problems/bus-routes/description/?envType=daily-question&envId=2023-11-12

class BusRoutes_815:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = []
        source_routes, target_routes = set(), set()
        for i in range(len(routes)):
            routes[i].sort()
            graph.append([])
            if source in routes[i]:
                source_routes.add(i)
            if target in routes[i]:
                target_routes.add(i)

        def haveCommonStop(route1: List[int], route2: List[int]) -> bool:
            p1, p2 = 0, 0
            while p1 < len(route1) and p2 < len(route2):
                if route1[p1] == route2[p2]:
                    return True
                if route1[p1] < route2[p2]:
                    p1 += 1
                else:
                    p2 += 1
            return False

        def create_graph():
            for i in range(len(routes)):
                for j in range(i + 1, len(routes)):
                    if haveCommonStop(routes[i], routes[j]):
                        graph[i].append(j)
                        graph[j].append(i)
        
        
        create_graph()

        q = list(source_routes)
        vis = set(source_routes)
        count = 1

        while q:
            size = len(q)
            for i in range(size):
                route = q.pop(0)
                if route in target_routes:
                    return count
                for nxt_route in graph[route]:
                    if not nxt_route in vis:
                        vis.add(nxt_route)
                        q.append(nxt_route)
            count += 1
        return -1
