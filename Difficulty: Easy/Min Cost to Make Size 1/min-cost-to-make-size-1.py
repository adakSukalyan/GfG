class Solution:
    def cost(self, arr):
        #code here
        n= len(arr)
        m=min(arr)
        return m*(n-1)