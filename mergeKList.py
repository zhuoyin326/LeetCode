# to use priority queue
import heapq

heap = []
heapq.heappush(heap, (5, 1, 'write code'))
heapq.heappush(heap, (7, 2, 'release product'))
heapq.heappush(heap, (1, 3, 'write spec'))
heapq.heappush(heap, (3, 4, 'create tests'))
heapq.heappop(heap)
heapq.heappop(heap)
heapq.heappop(heap)
heapq.heappop(heap)


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
        pq = []
        # iterate over the lists and push the first node of each list to the queue
        for i, l in enumerate(lists):
            # check if the list is not empty
            if l: 
                print("index i:", i, "ListNode's value:", l.val, "ListNode:", l, end="\n")
                # push a tuple of (value, index, node)
                heapq.heappush(pq, (l.val, i, l))
        # while the queue is not empty
        while pq:
            # pop the smallest node from the queue
            val, i, node = heapq.heappop(pq)
            print("index i:", i, "ListNode's value:", val, "ListNode:", l, end="\n")
            # append it to the merged list
            lastListNode.next = node
            # move the pointer to the next node
            lastListNode = lastListNode.next
            # if the popped node has a next node
            if node.next:
                # push it to the queue
                heapq.heappush(pq, (node.next.val, i, node.next))
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