class Solution(object):
    def generate(self, numRows):
        if numRows==0:
            return []
        if numRows==1:
        	return [[1]]
        if numRows==2:
        	return [[1],[1,1]]
        totalList=[[1],[1,1]]
        for i in range(0,numRows):
            list=map(lambda x,y : x+y, totalList[-1][1:], totalList[-1][:-1])
            list.append(1)
            list.insert(0,1)
            totalList.append(list)
        return totalList


class Solution(object):
    def generate(self, numRows):
        if numRows==0:
            return []
        totalList=[]
        for i in range(numRows):
            if i==0:
                totalList.append([1])
            elif i==1:
                totalList.append([1,1])
            else:
                xList=[1]
                for j in range(1,len(totalList[i-1])):
                    xList.append(totalList[i-1][j-1]+totalList[i-1][j])
                xList.append(1)
                totalList.append(xList)
        return totalList
