class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        number=0
        #可以拓展数组！！！！
        flowerbed=[0]+flowerbed+[0]
        if n==0: return True
        for i in range(1,len(flowerbed)-1):
            if  flowerbed[i]==flowerbed[i+1]==flowerbed[i-1]==0:
                n-=1
                flowerbed[i]=1
            if n==0: return True  
        return False