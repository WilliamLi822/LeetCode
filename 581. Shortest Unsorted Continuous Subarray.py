class Solution(object):
    def findUnsortedSubarray(self, nums):
        OriginNums=nums[:]
        nums.sort()
        start=end=-1
        if len(nums)==1:return 0
        for i in range(len(nums)):
            if start==-1 and nums[i]!=OriginNums[i]: 
                start=i
            if end==-1 and nums[len(nums)-i-1]!=OriginNums[len(nums)-i-1]: 
                end=len(nums)-i-1
        if start!=-1 and end!=-1:
            return  end-start+1
        else:
            return 0