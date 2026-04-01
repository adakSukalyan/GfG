from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        res=[]
        if not head:
            return res
        left=head
        right=head
        while right.next:
            right=right.next
        while left.data < right.data:
            if left.data + right.data == target:
                res.append([left.data,right.data])
                left=left.next
                right=right.prev
            elif left.data + right.data < target:
                left=left.next
            elif left.data + right.data > target:
                right=right.prev
        return res