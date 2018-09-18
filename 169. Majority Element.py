class Solution(object):
    def majorityElement(self, nums):
        if len(nums)==1:
        	return nums[0]
        nums.sort()
        count=1
        for end in range(1,len(nums)):
            if nums[end]!=nums[end-1]:
                if count>len(nums)/2:
                    return nums[end-1]
                else: count=1
            count+=1
        return nums[len(nums)-1]
        



class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=1
        nums.sort()
        if len(nums)==1:
            return nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                count+=1
            else: 
                count=1
            if count>=(len(nums)+1)/2:
                return nums[i]
                




class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]