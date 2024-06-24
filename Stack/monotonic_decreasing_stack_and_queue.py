"""
Monotonic Decreasing Queue
A monotonic decreasing queue is a data structure where the elements are maintained in decreasing order from the front to the back of the queue. This means that each element in the queue is smaller than or equal to the previous element.
"""

from collections import deque

class MonotonicDecreasingQueue:
    def __init__(self):
        self.queue = deque()
    
    def push(self, value):
        while self.queue and self.queue[-1] < value:
            self.queue.pop()
        self.queue.append(value)
    
    def pop(self):
        self.queue.popleft()
    
    def front(self):
        return self.queue[0] if self.queue else None

    def __str__(self):
        return str(list(self.queue))

# Example usage
md_queue = MonotonicDecreasingQueue()
md_queue.push(5)
md_queue.push(3)
md_queue.push(4)  # This will remove 3 before adding 4
md_queue.push(2)
print(md_queue)   # Output: [5, 4, 2]
md_queue.pop()
print(md_queue)   # Output: [4, 2]


"""
Monotonic Decreasing Stack
A monotonic decreasing stack is a data structure where the elements are maintained in decreasing order from the top to the bottom of the stack. This means that each element in the stack is smaller than or equal to the previous element.
"""

class MonotonicDecreasingStack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        while self.stack and self.stack[-1] < value:
            self.stack.pop()
        self.stack.append(value)
    
    def pop(self):
        if self.stack:
            self.stack.pop()
    
    def top(self):
        return self.stack[-1] if self.stack else None

    def __str__(self):
        return str(self.stack)

# Example usage
md_stack = MonotonicDecreasingStack()
md_stack.push(5)
md_stack.push(3)
md_stack.push(4)  # This will remove 3 before adding 4
md_stack.push(2)
print(md_stack)   # Output: [5, 4, 2]
md_stack.pop()
print(md_stack)   # Output: [5, 4]

