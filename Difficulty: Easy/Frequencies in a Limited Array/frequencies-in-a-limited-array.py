class Solution:
    def frequencyCount(self, arr):
        newarr=[0]*len(arr)
        for i in range(len(arr)):
            newarr[arr[i]-1]+=1
        return newarr

