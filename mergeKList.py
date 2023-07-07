import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    if not lists:
        return None

    # Custom comparison function for ListNode objects
    def compare_nodes(node1, node2):
        return node1.val - node2.val

    # Initialize the priority queue
    pq = []
    heapq.heapify(pq)

    # Push the head of each linked list into the priority queue
    for head in lists:
        if head:
            heapq.heappush(pq, (head.val, head))

    # Create a dummy node to build the merged list
    dummy = ListNode(0)
    current = dummy

    # Pop the smallest element from the priority queue and append it to the merged list
    while pq:
        _, node = heapq.heappop(pq)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(pq, (node.next.val, node.next))

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

# Merge the linked lists
merged = mergeKLists([list1, list2, list3])

# Print the merged list
while merged:
    print(merged.val, end=" ")
    merged = merged.next