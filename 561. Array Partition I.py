class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        x=0
        for i in range (0,len(nums),2):
            x+=nums[i]
        return x





class Solution(object):
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])


