class Solution(object):
    def findMaxAverage(self, nums, k):
        tmp=0
        Max=0
        if len(nums)==1: return nums[0]
        for i in range(k,len(nums)):
            tmp+=nums[i]-nums[i-k]
            Max=max(Max,tmp)
        return (Max+sum(nums[0:k]))/float(k)
        