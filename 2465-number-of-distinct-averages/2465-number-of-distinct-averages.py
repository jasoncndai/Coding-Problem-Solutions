class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        averages, n = set(), len(nums)
        nums.sort()
        for i in range(n//2):
            averages.add((nums[n-i-1] + nums[i]) / 2)
            print(averages)
        return len(averages)