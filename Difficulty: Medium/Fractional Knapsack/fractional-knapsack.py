class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        n=len(val)
        items=[[val[i],wt[i]] for i in range(n)]
        
        items.sort(key=lambda x: x[0]/x[1],reverse=True)
        
        currentcapacity=capacity
        res=0
        for i in range (n):
            
            if items[i][1] <= currentcapacity:
                res+=items[i][0]
                currentcapacity-= items[i][1]
            else:
                res+=(items[i][0]/items[i][1])*currentcapacity
                break
        return res
                
                
            