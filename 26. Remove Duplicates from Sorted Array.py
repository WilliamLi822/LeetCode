class Solution(object):
    def removeDuplicates(self, nums):
        """
        """
        if nums==[]:
            return 0
        site=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[site]=nums[i]
                site+=1
        return site
        