'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        #Code here
        if not head :
            return False
        p=head
        if head.data == key:
            return True
        while p.next!=None:
            p=p.next
            if key == p.data:
                return True
        else:
            return False
        