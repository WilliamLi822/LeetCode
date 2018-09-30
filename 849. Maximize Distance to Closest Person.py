class Solution(object):
    def maxDistToClosest(self, seats):
    	distance=0
    	maxdistance=0
    	site=0
    	for i in range(len(seats)):
    		if seats[i]==0:
    			distance+=1
    			if maxdistance<distance:
    				site=i
    		elif maxdistance<distance:
    			maxdistance=distance
    			site=i-distance/2
    			distance=0
    	return site