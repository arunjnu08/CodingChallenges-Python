# https://leetcode.com/problems/find-the-winner-of-an-array-game/description/?envType=daily-question&envId=2023-11-05

class FindTheWinnerOfAnArrayGame_1535:
    def getWinner(self, arr: List[int], k: int) -> int:
        win = 0
        ele = arr[0]
        for x in arr[1:]:
            if ele < x:
                win = 0
                ele = x
            win += 1
            if win == k:
                return ele
        return ele
