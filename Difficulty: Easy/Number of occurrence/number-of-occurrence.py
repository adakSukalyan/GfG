class Solution:
    def countFreq(self, arr, target):
        count=0
        for i in range(len(arr)):
            if target ==arr[i]:
                count+=1
        return count
        