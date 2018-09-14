class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)==0:
            return True
        dayu=0;
        xiaoyu=0;
        for i in range(len(A)-1):
            if A[i]>A[i+1]: dayu=1
            elif A[i]<A[i+1]: xiaoyu=1
            if dayu and xiaoyu: return False
        return True

