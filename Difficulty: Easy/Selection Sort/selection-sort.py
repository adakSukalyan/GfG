class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                min = arr[i]
                max = arr[j]
                if (min<max):
                    temp=arr[j]
                    arr[j]=arr[i]
                    arr[i]=temp
        return arr    