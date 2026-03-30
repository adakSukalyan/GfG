"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        
        if not head:
            return None 
        p=head
        q=head
        count=1
        while p.next!=None:
            p=p.next
            count+=1
        mid=count//2
        left=0
        right=count
        while left<mid and right > left:
            temp=p.data
            p.data=q.data
            q.data=temp
            p=p.prev
            q=q.next
            left+=1
            right-=1
            
        return head