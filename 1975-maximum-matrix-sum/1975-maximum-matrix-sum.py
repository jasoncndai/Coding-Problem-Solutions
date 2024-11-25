class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # track absolute sum, find number of negative elements, and track smallest element
        maximum_sum = 0
        minimum_element = float(-inf)
        num_odd = 0
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] <= 0:
                    num_odd += 1
                if abs(minimum_element) - abs(matrix[i][j]) > 0:
                    minimum_element = matrix[i][j]
                maximum_sum += abs(matrix[i][j])
        # if negative elements is even then all can be made positive
        if num_odd % 2 == 0:
            return maximum_sum
        
        # if odd then one must be negative 
        # make the smallest element negative and add the negative elemetn twice to account for prev addition
        print(maximum_sum)
        print(minimum_element)
        maximum_sum += -2*abs(minimum_element)
        return maximum_sum
                    
                