# https://leetcode.com/problems/minimum-time-visiting-all-points/submissions/1111204536/?envType=daily-question&envId=2023-12-03

class MinimumTimeVisitingAllPoints_1266:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        pre, ans = 0, 0
        for i in range(1, len(points)):
            ans += max(abs(points[i][0] - points[pre][0]), abs(points[i][1] - points[pre][1]))
            pre = i
        return ans
