'''
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
'''
class Solution:
    def getCount(self, head):
        # code here
        if not head:
            return 0
        p=head
        count=1
        while (p.next!=None):
            count+=1
            p=p.next
        return count