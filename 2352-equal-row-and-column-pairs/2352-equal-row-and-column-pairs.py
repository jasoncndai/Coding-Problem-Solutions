class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Intuition: Put all the rows in a hash/set
        # compare them with the columns in grid, if equal, increment count
        rows = {}
        count = 0
        for row in grid:
            rows[tuple(row)] = rows.get(tuple(row), 0) + 1
        for col in zip(*grid):
            count += rows.get(tuple(col), 0)
        return count