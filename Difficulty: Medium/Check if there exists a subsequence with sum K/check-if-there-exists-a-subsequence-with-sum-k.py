class Solution:
    def checkSubsequenceSum(self, N, arr, K):

        def solve(index, curr_sum):
            
            if curr_sum == K:
                return True
            if curr_sum > K:
                return False
            
            if index >= N:
                return False

            if solve(index + 1, curr_sum + arr[index]):
                return True

            if solve(index + 1, curr_sum):
                return True

            return False

        return solve(0, 0)