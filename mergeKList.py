# to use priority queue
import heapq

heap = []
heapq.heappush(heap, (5, 1, 'write code'))
heapq.heappush(heap, (7, 2, 'release product'))
heapq.heappush(heap, (1, 3, 'write spec'))
heapq.heappush(heap, (3, 4, 'create tests'))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print("\n")

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        # create a zeroth list node for the merged list
        zerothListNode = ListNode(-1)
        # create a pointer to the current node of the merged list
        lastListNode = ListNode(-1)
        # create a priority queue to store the nodes from each list
        priorityqueue = []
        # iterate over the lists and push the first node of each list to the queue
        for i, l in enumerate(lists):
            # check if the list is not empty
            if l: 
                print("heappush whinin the for loop")
                print("index i:", i, "List Node's value:", l.val, "List Node:", l)
                # push a tuple of (value, index, first node of each linked list)
                heapq.heappush(priorityqueue, (l.val, i, l))
        
        print("\n")
        
        # while the queue is not empty
        while priorityqueue:
            # pop the smallest node from the queue
            val, i, node = heapq.heappop(priorityqueue)
            print("heappop within the while loop")
            print("index i:", i, "current List Node's value:", val, "current List Node:", l, end="\n")
            # append it to the merged list
            lastListNode.next = node
            # move the pointer to the next node
            lastListNode = lastListNode.next
            # if the popped node has a next node
            if node.next:
                # push it to the queue
                heapq.heappush(priorityqueue, (node.next.val, i, node.next))
                print("heappush within the while lop")
                print("index i:", i, "next List Node's value", node.next.val, "next List Node's value", node.next,end = "\n")
                print("\n")
        # return the head of the merged list
        return zerothListNode.next

# Example usage
# Create linked lists
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)

# Create a Solution object
s = Solution()

# Merge the linked lists
merged = s.mergeKLists([list1, list2, list3])

# Print the merged list
while merged:
    print(merged.val, end=" ")
    merged = merged.next