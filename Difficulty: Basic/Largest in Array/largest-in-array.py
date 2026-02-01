class Solution:
    def largest(self, arr):
        l=arr[0]
        for i in range(1,len(arr)):
            if l<arr[i]:
                l=arr[i]
        return l