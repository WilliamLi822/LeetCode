class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MaxNum=float('-inf')
        SecondMaxNum=float('-inf')
        ThirdMaxNum=float('-inf')
        if len(nums)<3: return max(nums)
        for i in range(len(nums)):
            if  nums[i]>MaxNum:
                MaxNum,SecondMaxNum,ThirdMaxNum=nums[i],MaxNum,SecondMaxNum
            elif MaxNum>nums[i]>SecondMaxNum:
                SecondMaxNum,ThirdMaxNum=nums[i],SecondMaxNum
            elif SecondMaxNum>nums[i]>ThirdMaxNum:
                ThirdMaxNum=nums[i]
        if ThirdMaxNum!=float('-inf'):
            return ThirdMaxNum
        else: return MaxNum