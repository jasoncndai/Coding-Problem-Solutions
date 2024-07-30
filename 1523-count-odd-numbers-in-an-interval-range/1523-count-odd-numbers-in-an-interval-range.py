class Solution:
    def countOdds(self, low: int, high: int) -> int:
        range = high - low + 1
        if range % 2 == 0:
            return math.floor(range / 2)
        else:
            # Either both even or both odd
            if low % 2 == 0 and high % 2 == 0:
                return math.floor(range / 2)
            else:
                return math.floor(range / 2) + 1
            
        