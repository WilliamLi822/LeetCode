class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix)-1):
        	length=len(matrix[i])
        	if matrix[i][:-1]!=matrix[i+1][1:]:
        		return False
        return True
