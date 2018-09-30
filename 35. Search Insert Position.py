class Solution(object):
    def searchInsert(self, nums, target):
    	for i in range(len(nums)):
    		if nums[i]==target:
    			return i
    		if nums[i]>target:
    			return i
    	return len(nums)

#本质是数组查找，可以应用二分法

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
                
        return l