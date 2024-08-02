class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        averages = set()
        while len(nums) > 0:
            min = 99999
            max = 0
            for num in nums:
                if num < min:
                    min = num
                if num > max:
                    max = num
            nums.remove(min)
            nums.remove(max)
            averages.add((max + min) / 2)
            
                
        return len(averages)