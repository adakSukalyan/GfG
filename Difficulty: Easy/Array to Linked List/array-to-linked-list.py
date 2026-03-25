'''
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def arrayToList(self, arr):
        # code here
        if not arr:
            return None
        head=Node(arr[0])
        current=head
        for i in range(1,len(arr)):
            new=Node(arr[i])
            current.next=new
            current=new
        return head
            
        