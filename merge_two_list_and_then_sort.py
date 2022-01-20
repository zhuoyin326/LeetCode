"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""
# Joe's Algorithm:
# Merge two lists A and B into one list C
# Sorted the elements in list C
# Print out the sorted elements of list C

listA = [1, 2, 4]
listB = [1, 3, 4]

listA = []
listB = []

listA = []
listB = [0]

"""code A does not work"""
def mergeList(listA, listB):
    listC = listA + listB
    listC.sort()
    return print(ListC)
mergeList(listA, listB)


"""code B does not work"""
def mergeList(listA, listB):
    listC = listA + listB
    listC.sort()
    output = print(ListC)
    return output
mergeList(listA, listB)


"""code C works"""
def mergeList(listA, listB):
    listC = listA + listB
    listC.sort()
    return listC
mergeList(listA, listB)

