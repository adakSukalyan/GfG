class Solution:
    def buyMaximumProducts(self, k: int, prices: list[int]) -> int:
        # code here
        n=len(prices)
        arr=[]
        for i in range(n):
            arr.append([prices[i],i+1])
        arr.sort(key=lambda x:x[0])
        
        total_p=0
        for i in range(n):
            p=min(arr[i][1], k//arr[i][0])
            k-=arr[i][0]*p
            total_p+=p
        return total_p
        