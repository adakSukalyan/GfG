class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        ele=arr[0]
        for i in range(1,len(arr)):
            if ele>arr[i]:
                return False
            ele=arr[i]
        return True