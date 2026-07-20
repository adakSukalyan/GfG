class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort()

        temp = []
        i = 0
        j = len(arr) - 1

        while i <= j:
            if i == j:
                temp.append(arr[i])
            else:
                temp.append(arr[i])
                temp.append(arr[j])
            i += 1
            j -= 1

        arr = temp
        
        
        n=len(arr)
        sum=0
        for i in range(n-1):
            sum+=abs(arr[i]-arr[i+1])
        sum+=abs(arr[n-1] -arr[0])
        return sum