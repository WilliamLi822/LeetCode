class Solution(object):
    def flipAndInvertImage(self,A):
        for i in A:
            for j in range((len(i) + 1)/2):
                i[j], i[len(i) - j - 1] =i[len(i) - j - 1],i[j]
        for i in A:
            for j in range((len(i))):
                if i[j]:
                    i[j]=0
                else:
                    i[j]=1
        return A



class Solution(object):
    def flipAndInvertImage(self,A):
        list=[]
        for i in A:
            list.append([0 if x == 1 else 1 for x in i][::-1])
        return list



class Solution(object):
    def flipAndInvertImage(self, A):
        return [[1^i for i in row[::-1]] for row in A]


