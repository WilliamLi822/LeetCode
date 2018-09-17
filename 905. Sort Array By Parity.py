class Solution(object):
    def sortArrayByParity(self, A):
        list=[x for x in A if x%2==0]+[x for x in A if x%2==1]
        return list