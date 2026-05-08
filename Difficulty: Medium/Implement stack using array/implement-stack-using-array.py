class myStack:
    def __init__(self, n):
        # Define Data Structures
        self.stack=[]
        self.size=n

    
    def isEmpty(self):
        # Check if stack is empty
        if len(self.stack)==0:
            return True
        else:
            return False

    
    def isFull(self):
        # Check if stack is full
        if len(self.stack)==self.size:
            return True
        else:
            return False

    
    def push(self, x):
        # Insert x at the top of the stack
        if not self.isFull():
            self.stack.append(x)

    
    def pop(self):
        # Removes an element from the top of the stack
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return -1
    def peek(self):
        # Returns the top element of the stack
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return -1