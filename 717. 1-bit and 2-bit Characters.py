class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        count=0
        for i in range(len(bits)-2,-1,-1):
        	if bits[i]==1: count+=1
        	else: break
        if count%2==1: return False
        else: return True