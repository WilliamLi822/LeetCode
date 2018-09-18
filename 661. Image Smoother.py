class Solution(object):
    def imageSmoother(self, M):
    	#X=[0]*len(M[0])
    	#N=[X]*len(M)
        
        Row=len(M)
    	Col=len(M[0])
        N = [[0] * Col for _ in M]
        
        for r in range(Row):
        	for c in range(Col):
        		count =0
        		for r_t in range(r-1,r+1,1):
        			for c_t in range(c-1,c+1,1):
        				if 0<=r_t<Row and 0<=c_t<Col:
        					N[r][c]+=M[r_t][c_t]
        					count+=1
                N[r][c]/=count
    	return N




class Solution(object):
    def imageSmoother(self, M):
        R, C = len(M), len(M[0])
        ans = [[0] * C for _ in M]

        for r in xrange(R):
            for c in xrange(C):
                count = 0
                for nr in (r-1, r, r+1):
                    for nc in (c-1, c, c+1):
                        if 0 <= nr < R and 0 <= nc < C:
                            ans[r][c] += M[nr][nc]
                            count += 1
                ans[r][c] /= count

        return ans