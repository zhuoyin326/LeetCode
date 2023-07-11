# to use priority queue
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        # create a dummy head node for the merged list
        dummy = ListNode()
        # create a pointer to the current node of the merged list
        curr = dummy
        # create a priority queue to store the nodes from each list
        pq = []
        # iterate over the lists and push the first node of each list to the queue
        for i, l in enumerate(lists):
            # check if the list is not empty
            if l: 
                print("index i:", i, "ListNode's value:", l.val, "ListNode:", l, end="\n")
                heapq.heappush(pq, (l.val, i, l)) # push a tuple of (value, index, node)
        # while the queue is not empty
        while pq:
            # pop the smallest node from the queue
            val, i, node = heapq.heappop(pq)
            # append it to the merged list
            curr.next = node
            # move the pointer to the next node
            curr = curr.next
            # if the popped node has a next node
            if node.next:
                # push it to the queue
                heapq.heappush(pq, (node.next.val, i, node.next))
        # return the head of the merged list
        return dummy.next

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