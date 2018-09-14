class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        list=[]
        for i in range(len(A[0])):
            list.append([A[j][i] for j in range(len(A))])
        return list


        
class Solution(object):
    def transpose(self, A):         
        return list(zip(*A))