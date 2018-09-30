class Solution(object):
    def rotate(self, nums, k):
        s=k%len(nums)
        for i in range(s):
            nums.insert(0,nums.pop(len(nums)-1))
        


class Solution(object):
    def rotate(self, nums, k):
        s=k%len(nums)
        x=nums[:]
        for i in range(len(nums)):
            nums[(i+s)%len(nums)]=x[i]
        


class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]