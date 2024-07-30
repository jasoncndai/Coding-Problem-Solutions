class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # subtract num of odds from 1 to low -1 from 1 to high
        # +1 to each and // 2, +1 accounts for even or odd number in count
        return (high + 1) // 2 - low // 2
        