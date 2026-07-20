class Solution:
    def minMaxCandy(self, prices, k):
        # code here
        prices.sort()
        
        n=len(prices)
        
        i , end= 0,n-1
        
        mincost=0
        while(i<=end):
            mincost+=prices[i]
            i+=1
            
            end-=k
            
        maxcost=0
        i,start =n-1,0
        while(i>=start):
            maxcost+=prices[i]
            i-=1
            
            start+=k
        return [mincost,maxcost]