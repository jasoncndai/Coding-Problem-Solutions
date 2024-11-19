class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Use a hashmap to store values of target-num in hashmap
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target-num], i]
            hashmap[num] = i
        