class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.queue=[]
        self.size=n

    
    def isEmpty(self):
        # Check if queue is empty
        if len(self.queue)==0:
            return True
        else:
            return False
    
    def isFull(self):
        # Check if queue is full
        if len(self.queue)==self.size:
            return True
        else:
            return False
    
    
    def enqueue(self, x):
        # Enqueue
        if not self.isFull():
            self.queue.append(x)

    
    def dequeue(self):
        # Dequeue
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            return -1
    
    def getFront(self):
        # Get front element
        if not self.isEmpty():
            return self.queue[0]
        else:
            return -1
    
    def getRear(self):
        # Get rear element 
            if not self.isEmpty():
                return self.queue[-1]
            else:
                return -1
        