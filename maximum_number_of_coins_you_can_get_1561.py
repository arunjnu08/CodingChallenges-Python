# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/?envType=daily-question&envId=2023-11-24

class MaximumNumberOfCoinsYouCanGet_1561:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        return sum(piles[n // 3 : n : 2])
