class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f1=0
        f2=0
        for x in cost:
            f1,f2=min(f1,f2)+x,f1
        return min(f1,f2)
        
        #动态规划！！！！！！！！


    def func(cost):
        pre, cur = cost[0], cost[1]
        for i in range(2, len(cost)):
            pre, cur = cur, min(pre, cur) + cost[i]
        return min(pre,cur)