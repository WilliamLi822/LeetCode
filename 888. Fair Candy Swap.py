class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        cha=(sum(B)-sum(A))/2
        B=set(b)##!!!!!!!!!!!一定要先去重以节约时间
        for i in A:
        	if cha+i in B:
        		return [i,cha+i]
        return