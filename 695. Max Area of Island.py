class Solution(object):
    def maxAreaOfIsland(self, grid):
        max=0
        for i in range(len(grid)):
        	for j in range(len(grid[i])):
        		count=self.forOne(grid,i,j,0)
        		if max<=count: max=count
        return max
    
    def forOne(self,grid,i,j,count):
        if grid[i][j]==1:
            count+=1
            grid[i][j]=0
            if i!=0 :
                count=self.forOne(grid,i-1,j,count)
            if i!=len(grid)-1:
    		    count=self.forOne(grid,i+1,j,count)
            if j!=0:
                count=self.forOne(grid,i,j-1,count)
            if j!=len(grid[0])-1:
                count=self.forOne(grid,i,j+1,count)
    	    return count
        else: 
            return count

