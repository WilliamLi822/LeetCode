class Solution(object):
    def findDisappearedNumbers(self, nums):
        list=[]
        s=set(nums)
        for i in range(len(nums)):
        	if i+1 not in s:
        		list.append(i+1)
        return list

        #时间过长！！


class Solution(object):
    def findDisappearedNumbers(self, nums):
    	return list(set(range(1,len(nums)+1))-set(nums))

