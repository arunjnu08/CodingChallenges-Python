# https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/submissions/1094067817/?envType=daily-question&envId=2023-11-08

class DetermineIfACelIsReachableatAGivenTime_2849:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        return False if sx == fx and sy == fy and t == 1 else max(abs(sx - fx), abs(sy - fy)) <= t
