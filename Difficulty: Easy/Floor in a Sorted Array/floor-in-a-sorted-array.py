class Solution:
    def findFloor(self, arr, x):
        # code here
        i=0
        res=0
        while(i<len(arr) and arr[i]<=x):
            res=arr[i]
            i+=1
        return i-1