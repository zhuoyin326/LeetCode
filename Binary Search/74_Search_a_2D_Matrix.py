"""
Joe’s code problem on November 11th, 2023

Title: 74. Search a 2D Matrix
Tag: Array, Binary Search,Matrix
Difficulty: Medium

You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104    
    
"""
class Solution:
    def searchMatrix(matrix, target):
        rowLength = len(matrix)
        columnLength = len(matrix[0])
        # The left boundary of the list is 0.
        left = 0
        # The right boundary of the list is the product of the total number of columns and the total number of rows in the matrix, minus one.
        right = rowLength*columnLength-1
		# We continue the while loop as long as the left boundary is less than or equal to the right boundary:
        while left <= right:
			# Calculate the middle point using the left and right pointers.
            mid = left + (right - left)//2
			# Obtain the value of the matrix element at the middle point.
			# By floor dividing the index by the total number of columns in the matrix, we obtain a corresponding row number. 
            # By taking the modulus of the index with the total number of columns in the matrix, we obtain a corresponding column number.
            element = matrix[mid//columnLength][mid % columnLength]
			# If the element is equal to the target, return True.
            if element == target:
                return True
			# If the element is less than the target, we search the upper range by updating the left boundary to ‘mid+1’. 
            elif element < target:
                left = mid + 1
			# If the element is greater than the target, we search the lower range by updating the right boundary to ‘mid-1’. 
            else: 
                right = mid -1
		# When the while loop finishes, this means we did not find the target, and we then return False.
        return False