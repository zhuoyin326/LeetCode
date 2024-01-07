"""

Joe’s code problem on December 30th, 2023

Title: 746. Min Cost Climbing Stairs
Tag: Array, Dynamic Programming
Difficulty: Easy

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1. Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 
Constraints:
2 <= cost.length <= 1000
0 <= cost[i] <= 999
  
"""

class Solution:
    def minCostClimbingStairs(self, cost):
        minCost = [0]*(len(cost)+1)
        for i in range(2, len(cost)+1):
            minCost[i] = min(minCost[i-1]+cost[i-1],minCost[i-2]+cost[i-2])
        return minCost[-1]
 
class Solution:   
    def minCostClimbingStairs(self, cost):
        one = 0
        two = 0
        for i in range(2, len(cost)+1):
            temp = one
            one = min(one+cost[i-1], two+cost[i-2])
            two = temp
        return one