class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        start=0
        count=1
        Result=[]

        if len(S)<3:
        	return []
        for i in range(1,len(S)):
        	if S[i]==S[i-1]:
        		count+=1
        	else:
        		if count>=3:
        			Result.append([start,i-1])
        		count=1
        	if count==3:
        		start=i-2
        	if i == len(S)-1 and count>=3:
        			Result.append([start,i])
        return Result




class Solution(object):
    def largeGroupPositions(self, S):
        i, j, N = 0, 0, len(S)
        res = []
        while j < N:
            while j < N and S[j] == S[i]: j += 1
            if j - i >= 3: res.append((i, j - 1))
            i = j
        return res


class Solution(object):
    def largeGroupPositions(self, S):
        return [[r.start(), r.end() - 1] for r in re.finditer(r'(\w)\1{2,}', S)]