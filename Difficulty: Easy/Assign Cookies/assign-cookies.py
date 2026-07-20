class Solution:
    def maxChildren(self, greed, cookie):
        #code here
        greed.sort()
        cookie.sort()
        i=0
        j=0
        while i<len(greed) and j<len(cookie):
            if cookie[j]>=greed[i]:
                i+=1
            j+=1
        return i