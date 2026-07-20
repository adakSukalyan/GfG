class Solution:

    def rotationCount(self, r, d):
        """ code here """
        res=0
        while(r!=0 or d!=0):
            rem=r%10
            r//=10
            dem=d%10
            d//=10
            res+=min(abs(rem-dem), 10-abs(rem-dem))
        
        return res