"""
Monotonic Decreasing Queue
A monotonic decreasing queue is a data structure where the elements are maintained in decreasing order from the front to the back of the queue. This means that each element in the queue is smaller than or equal to the previous element.
"""

from collections import deque
def monotonicDecreasingQueue(list):
    queue = deque()
    for x in list:
        # While the deque is not empty and the last element is smaller than x
        while queue and queue[-1] < x:
            # Remove the last element
            queue.pop()
        # Append x to the deque
        queue.append(x)
    return queue

# Example usage
list = [7, 5, 3, 1, 2, 4]
queue = monotonicDecreasingQueue(list)
print(queue)
# Pop an element from the current queue
queue.popleft()
print(queue)
# Pop another element from the current queue
queue.popleft()
print(queue)


"""
Monotonic Decreasing Stack
A monotonic decreasing stack is a data structure where the elements are maintained in decreasing order from the top to the bottom of the stack. This means that each element in the stack is smaller than or equal to the previous element.
"""

def monotonicDecreasingStack(list):
   stack = []
   for x in list:
       # While the stack is not empty and the last element is smaller than x
       while stack and stack[-1] < x:
           # Remove the last element
           stack.pop()
       # Append x to the stack
       stack.append(x)
   return stack


# Example usage
list = [7, 5, 3, 1, 2, 4]
stack = monotonicDecreasingStack(list)
print(stack)
# Pop an element from the current stack
stack.pop()
print(stack)
# Pop another element from the current stack
stack.pop()
print(stack)


