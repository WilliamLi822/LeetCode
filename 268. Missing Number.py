class Solution(object):
    def missingNumber(self, nums):
        lis11t=list(set(range(0, len(nums)+1)) - set(nums))
        return lis11t[0]


class Solution(object):
	def missingNumber(self, nums):
	    n = len(nums)
	    return n * (n+1) / 2 - sum(nums)

