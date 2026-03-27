'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    def insertAtPos(self, head, p, x):
        # Code Here
        new=Node(x)
        if not head:
            head=new
            return head
        else:
            curr=head
            for i in range(p):
                curr=curr.next
            new.next=curr.next
            new.prev=curr
            curr.next=new
        return head
                