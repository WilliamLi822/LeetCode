class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count0=nums.count(0)
        i=0
        while i<len(nums):
            if nums[i]==0:
                nums.remove(0)
                i-=1
            i+=1
        for j in range(count0):
            nums.append(0)


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last0 = 0
        for i in range(0,len(nums)):
            if (nums[i]!=0):
                nums[i],nums[last0] = nums[last0],nums[i]
                last0+=1


nums.sort(key= lambda x: 1 if x == 0 else 0)


nums[:]=[x for x in nums if x!=0]+[x for x in nums if x==0]



class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                t = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = t
                slow+=1
            fast+=1



class Solution(object):
    def moveZeroes(self, nums):
        
        zerolist=[]
        for i in range(len(nums)):
            if nums[i]==0:
                zerolist.append(i)
            if nums[i]!=0 and len(zerolist)!=0:
                nums[zerolist.pop(0)]=nums[i]
                nums[i]=0
                zerolist.append(i)