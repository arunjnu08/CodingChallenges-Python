# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/description/?envType=daily-question&envId=2023-11-07

class EliminateMaximumNumberOfMonsters_1921:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        for i in range(len(dist)):
            dist[i] = ceil(dist[i] / speed[i])
        dist.sort()
        res = 0
        time = 0
        for x in dist:
            x -= time
            time += 1
            if x > 0:
                res += 1
            else:
                break
        return res
