# November 6, 2023
# https://leetcode.com/problems/seat-reservation-manager/?envType=daily-question&envId=2023-11-06

class SeatManager:
    def __init__(self, n: int):
        self.st = set()
        self.ct = 0

    def reserve(self) -> int:
        if self.st:
            ans = min(self.st)
            self.st.remove(ans)
            return ans
        self.ct += 1
        return self.ct

    def unreserve(self, seatNumber: int) -> None:
        self.st.add(seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)