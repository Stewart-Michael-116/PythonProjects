# A Queue using two stacks

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.size = 0
        self.stack1 = self.Stack()
        self.stack2 = self.Stack()

    def enQueue(self, data):
        self.stack1.push(data)

    def deQueue(self):

        if self.stack1.size == 0 and self.stack2.size == 0:
            return
        
        elif self.stack2.size == 0:
            while self.stack1.size != 0:
                self.stack2.push(self.stack1.pop())
        
        return(self.stack2.pop())
    
        
    class Stack: 
        def __init__(self): 
            self.top = None 
            self.size = 0

        def push(self, data): 
            node = Node(data) 
            if self.top: 
                node.next = self.top 
                self.top = node                 
            else: 
                self.top = node 
            self.size += 1 

        def pop(self): 
            if self.top: 
                data = self.top.data 
                self.size -= 1  
                if self.top.next: 
                    self.top = self.top.next 
                else: 
                    self.top = None 
                return data 
            else: 
                return None



queue = Queue()

queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)
queue.enQueue(4)

print(queue.deQueue())
print(queue.deQueue())

queue.enQueue(4)
queue.enQueue(5)

print(queue.deQueue())
print(queue.deQueue())