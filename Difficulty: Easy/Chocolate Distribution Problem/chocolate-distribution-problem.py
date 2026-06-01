class Solution:
    def findMinDiff(self, arr, m):
        arr.sort()
        ans = float('inf')

        for i in range(len(arr) - m + 1):
            ans = min(ans, arr[i + m - 1] - arr[i])

        return ans