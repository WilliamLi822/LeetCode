class Solution(object):
    def matrixReshape(self, nums, r, c):
        lenR=len(nums)
        lenC=len(nums[0])
        if lenR*lenC < r*c:
        	return nums
        count=0
        result=[]
        list=[]
        for i in range(lenR):
        	for j in range(lenC):
        		list.append(nums[i][j])
        		count+=1
        		if count==c:
        			result.append(list)
        			list=[]
        			count=0
        return result



class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # Invalid input
        if nums == [] or nums == [[]]:
            return nums
        m, n = len(nums), len(nums[0])
        if m*n != r*c or (m == r and n == c):
            return nums
        temp = []
        for row in nums:
            temp.extend(row)
        ans = []
        for i in range(r):
            ans.append(temp[i*c:(i+1)*c])
        return ans


class Solution(object):
    def matrixReshape(self, nums, r, c):
        if r * c != len(nums) * len(nums[0]):
            return nums
        else:
            items = [y for x in nums for y in x]
            return [items[x*c : ((x+1)*c)] for x in range(r)]