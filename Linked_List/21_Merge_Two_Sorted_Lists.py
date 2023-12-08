"""

Joe’s Code Problem on Jan 23rd, 2022:

Title: 21. Merge Two Sorted Lists
Tag: Linked List
Difficulty: Easy

Given the heads of two sorted linked lists list A and list B.
Merge the two lists in a one sorted list. This list should be made by splicing together the nodes of the first two lists. 
Return the head of the merged linked list.

Example 1:

Input: listA = [1, 2, 4], listB = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]

Example 2:
Input: listA = [], listB = []
Output: []

Example 3:
Input: listA = [], listB = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""

# definition for singly-linked list
class ListNode:
	# self refers to the instance of the class ListNode
	def _init_(self, val = 0, next = None):
		self.val = val
		self.next = next
  
class Solution:
	def mergeTwoLists(self, l1, l2):
		# define the 0th link node which points to the head of the merged linked list
		zerothListNode = ListNode(-1)

		# define last link node which points to the tail of the merged linked list
		lastListNode = ListNode(-1)

		# we continue the while loop at least one of the linked list is not None
		while l1 and l2:
			# if the current first node of the linked list A is either smaller than or equal to the current first node of linked list B
			if l1.val <= l2.val:
				# the next node of the merged linked list points to the current first node of the linked list A
				lastListNode.next = l1
				# remove the current first node from the linked list A
				l1 = l1.next
			# if the current first node of the linked list A is larger than the current first node of linked list B
			else:
				# the next node of the merged linked list points to the current first node of the linked list B
				lastListNode.next = l2
				# remove the current first node from the linked list B
				l2 = l2.next
			
			# we added one more node to the merged linked list, we should update the tail of the merged linked list
			lastListNode = lastListNode.next

		# we break the while loop when one of these two linked list is None
		# if the current the linked list A is not None, we update the current last link node to point to the current first node of linked list A
		if l1:
			lastListNode.next = l1
		# if the current the linked list B is not None, we update the current last link node to point to the current first node of linked list B
		else:
			lastListNode.next = l2

		# we return the first node of the merged linked list
		return zerothListNode.next

