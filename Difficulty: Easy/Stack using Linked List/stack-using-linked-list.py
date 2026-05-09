# Node class
''' class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None 
'''

# Stack class template
class myStack:

    def __init__(self):
        # Initialize your data members
        self.top = None
        self.count = 0

    def isEmpty(self):
        # Check if the stack is empty
        return self.top == None
        

    def push(self, x):
        # Adds element x to the top of the stack
        new = Node(x)
        new.next = self.top
        self.top = new
        self.count += 1
        

    def pop(self):
        # Removes an element from the top of the stack
        if self.isEmpty():
            return -1
        
        temp = self.top.data
        self.top = self.top.next
        self.count -= 1
        
        return temp


    def peek(self):
        # Returns the top element of the stack
        # If the stack is empty, return -1
        if self.isEmpty():
            return -1
        
        return self.top.data


    def size(self):
        # Returns the current size of the stack
        return self.count