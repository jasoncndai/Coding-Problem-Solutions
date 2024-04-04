class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # use a hashmap to store the frequency of each element
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        # use a set to store the unique frequencies
        freq_set = set()
        for key in freq:
            freq_set.add(freq[key])
        # if the length of the set is equal to the length of the hashmap, return True
        return len(freq_set) == len(freq)