class Solution(object):
    def maxSubArray(self, nums):
    	maxSum=0
    	Sum=-1
        if max(nums)<=0: return max(nums)
        
        for i in nums:
            if Sum>0:
                Sum+=i
                if Sum<=0: 
                    Sum=-1
                maxSum=max(maxSum,Sum)
            elif Sum==-1 and i>0:
                Sum=i
                maxSum=max(maxSum,Sum)
        
        maxSum=max(maxSum,Sum)
    	return maxSum



class Solution(object):
    def maxSubArray(self, nums):
        preSum = 0
        mx = float('-Inf')
        
        for num in nums:
            if preSum > 0:
                preSum += num
            else:
                preSum = num
            
            mx = max(mx, preSum)
        
        return mx


class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
                if nums[i-1] > 0:
                    nums[i] += nums[i-1]
            return max(nums)