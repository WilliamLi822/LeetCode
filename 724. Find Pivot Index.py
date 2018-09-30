class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        SumNum=sum(nums)
        count=0
        for i in range(len(nums)):
            SumNum-=nums[i]
            if count==SumNum:
                return i
            count+=nums[i]
        return -1


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        SumNum=sum(nums)
        count=0
        for i in range(len(nums)):
            count+=nums[i]
            if i>0: SumNum-=nums[i-1]
            if count==SumNum:
                return i
        return -1