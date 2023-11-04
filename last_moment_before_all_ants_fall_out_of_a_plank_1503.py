# https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/description/?envType=daily-question&envId=2023-11-04

class LastMomentBeforeAllAntsFallOutOfAPlank_1503:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left) if left else 0, n - min(right) if right else 0)
