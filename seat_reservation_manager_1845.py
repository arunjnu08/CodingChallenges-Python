# https://leetcode.com/problems/seat-reservation-manager/description/?envType=daily-question&envId=2023-11-06

class SeatManager:

    def __init__(self, n: int):
        self.pq = []
        self.last = 0

    def reserve(self) -> int:
        if self.pq:
            return heapq.heappop(self.pq)
        self.last += 1
        return self.last

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber == self.last:
            self.last -= 1
        else:
            heapq.heappush(self.pq, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
