'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        seen=set()
        if not head:
            return head
        p= head
        seen.add(p.data) 

        while p.next!=None:
            if p.next.data in seen:
                if p.next.next:
                    p.next.next.prev=p
                p.next=p.next.next
            else:
                seen.add(p.next.data)
                p=p.next
        return head