#User function Template for python3

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    def constructDLL(self, arr):
        # Code here
        n=len(arr)
        new=Node(arr[0])
        new.prev=None
        new.next=None
        self.head=new
        p=self.head
        for i in range(1,n):
            new=Node(arr[i])
            new.prev=p
            p.next=new
            p=p.next
        return self.head