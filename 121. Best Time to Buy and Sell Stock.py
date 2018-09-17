class Solution(object):
    def maxProfit(self, prices):
    	result=0
    	low=float'Inf'
    	for i in range(len(prices)):
    		if prices[i]<=low:
    			low=prices[i]
    		elif prices[i]-low>result:
    			result=prices[i]-low
    	return result