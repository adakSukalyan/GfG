#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        # code here
        count=0
        og=n
        while(n!=0):
            rem=n%10
            if rem!=0:
                if og%rem ==0:
                    count+=1
            n//=10
        return count