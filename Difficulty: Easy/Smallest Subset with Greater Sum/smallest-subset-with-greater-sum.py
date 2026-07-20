class Solution:
    def minSubset(self, arr):
        # code here
        arr.sort(reverse=True)
        n=len(arr)
        
        selected=0
        
        total=sum(arr)
        
        for i in range(n):
            
            selected+=arr[i]
            
            rem=total-selected
            
            if selected>rem:
        
                return i+1
