class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        sell=0
        for i in range(1,len(prices)):
        	if prices[i]>prices[i-1]:
        		sell+=prices[i]-prices[i-1]