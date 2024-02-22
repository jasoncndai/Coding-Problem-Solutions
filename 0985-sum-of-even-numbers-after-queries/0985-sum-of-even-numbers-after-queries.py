class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        S = sum(num for num in nums if num % 2 == 0)
        answer = []
        
        for val,index in queries:
            if nums[index] % 2 == 0: S -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0: S += nums[index]
            answer.append(S)
            
        return answer