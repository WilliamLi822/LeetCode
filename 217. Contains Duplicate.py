class Solution(object):
    def containsDuplicate(self, nums):
        if len(set(nums))==len(nums):return False
        else: return True



class Solution(object):
    def containsDuplicate(self, nums):
        Originlen=len(nums)
        numsA=set(nums)
        Newlen=len(numsA)
        if Newlen==Originlen:return False
        else: return True


hashmap也可以实现！！！！空间时间均为O(N)