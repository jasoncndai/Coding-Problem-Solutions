class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 1 and high % 2 == 1:
            return math.floor((high - low + 1) / 2) + 1
        else:
            return math.floor((high - low + 1) / 2)
            
        