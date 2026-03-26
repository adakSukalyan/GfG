'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        new=Node(x)
        if not head:
            head=new
            return head
        p=head
        while(p.next!=None):
            p=p.next
        p.next=new
        return head