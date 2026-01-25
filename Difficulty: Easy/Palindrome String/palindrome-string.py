class Solution:
    def isPalindrome(self, s):
        return self.palindrome(s,0,len(s)-1)
    def palindrome(self,s, l, r):
        if(l>=r):
            return True
        if(s[l]!=s[r]):
            return False
        return self.palindrome(s,l+1,r-1)