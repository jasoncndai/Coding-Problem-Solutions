class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        answer = []
        result = {}
        #remove duplicates
        nums1 = list(dict.fromkeys(nums1))
        nums2 = list(dict.fromkeys(nums2))
        nums3 = list(dict.fromkeys(nums3))
        for num in nums1:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        for num in nums2:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        for num in nums3:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        
        print(result)
        for num in result:
            if result[num] > 1:
                answer.append(num)
        return answer