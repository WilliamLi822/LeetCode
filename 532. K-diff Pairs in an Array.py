class Solution(object):
    def findPairs(self, nums, k):
        count=0
        dictNums={}
        for i in nums:
            dictNums[i]=0
        for i in nums:
            dictNums[i]+=1
        for i in dictNums:
            if k>0:
                if i+k in dictNums: count+=1
            if k==0:
                if dictNums[i]>1: count+=1
        return count