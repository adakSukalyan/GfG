# Node class
class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Queue class template
class myQueue:

    def __init__(self):
        # Initialize your data members
        self.queue=[]

    def isEmpty(self):
        # Return True if queue is empty, else False
        if len(self.queue)==0:
            return True
        else:
            return False

    def enqueue(self, x):
        # Add element x to the rear
        self.queue.append(x)
        
    def dequeue(self):
        # Remove the front element
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            return -1


    def getFront(self):
        # Return front element
        # return -1 if empty
        if not self.isEmpty():
            return self.queue[0]
        else:
            return -1
        


    def size(self):
        # Return current size
        return len(self.queue)
