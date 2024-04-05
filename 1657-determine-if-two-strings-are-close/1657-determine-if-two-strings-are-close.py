class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Things about both strings that are the same:
        # no characters unique to one word
        # need to have same frequency for characters 
        #   (doesn't haven't to be same character) e.g. 2 a's 1 b , 2 b's 1 a
        # create a hashmap for character frequency in both words
        map1 = {}
        map2 = {}
        for c in word1:
            if c in map1:
                map1[c] += 1
            else:
                map1[c] = 1
        for c in word2:
            if c in map2:
                map2[c] += 1
            else:
                map2[c] = 1
        
        # check if the characters are the same
        if set(map1.keys()) != set(map2.keys()):
            return False
        # check if the frequencies are the same
        if sorted(map1.values()) != sorted(map2.values()):
            return False
        return True
        
        
        