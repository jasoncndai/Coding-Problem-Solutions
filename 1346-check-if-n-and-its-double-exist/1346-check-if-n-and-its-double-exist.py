class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for j in arr:
            if 2 * j in seen or (j % 2 == 0 and j // 2 in seen):
                return True
            seen.add(j)
        return False
        