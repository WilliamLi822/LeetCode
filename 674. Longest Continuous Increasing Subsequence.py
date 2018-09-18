class Solution(object):
    def findLengthOfLCIS(self, nums):
        index=0
        maxcount=0
        if len(nums)<=1:
            return len(nums)
        
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]: index=i
            maxcount=max(i-index+1,maxcount)
        return maxcount
    

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=1
        maxcount=1
        if len(nums)<=1:
            return len(nums)
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                count+=1
            else:
                if count>maxcount:
                    maxcount=count
                count=1
            if count>maxcount:
                    maxcount=count
        return maxcount