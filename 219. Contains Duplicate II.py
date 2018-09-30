class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        
        Dic={}
        for i in range(len(nums)):
            if nums[i] in Dic:
                if i-Dic[nums[i]]<=k:
                    return True
            Dic[nums[i]]=i
        return False