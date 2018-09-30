class Solution(object):
    def dominantIndex(self, nums):
    	if len(nums)==1:
    		return 0
    	MaxNumber=max(nums)
    	MaxIndex=nums.index(MaxNumber)
    	for i in nums:
    		if i>MaxNumber/2:
    			return -1
    	return MaxIndex