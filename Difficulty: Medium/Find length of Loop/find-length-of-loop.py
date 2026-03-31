'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        seen=set()
        p=head
        q=p
        while p!=None:
            if p in seen :
                q=p
                break
            seen.add(p)
            p=p.next
        if p==None:
            return 0
        r=q
        count=1
        while q.next!=r:
            count+=1
            q=q.next
        return count