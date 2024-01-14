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

# Bottom-up Dynamic Programming (Tabulation)
class Solution:
    def minCostClimbingStairs(self, cost):
        # Initialize an array to store the minimum cost to reach each stair.
        # The length is len(cost) + 1 because we consider the "top" of the staircase as a step beyond the last.
        minCost = [0] * (len(cost) + 1)

        # Start iterating from the 2nd stair (index 2) because the minimum cost to reach the first two stairs (index 0 and 1) is 0.
        for i in range(2, len(cost) + 1):
            # For each stair, calculate the minimum cost by comparing the cost of taking a single step from the previous stair or taking a two-step jump from two stairs back.
            minCost[i] = min(minCost[i - 1] + cost[i - 1], minCost[i - 2] + cost[i - 2])

        # Return the minimum cost to reach the top of the staircase, which is beyond the last step in the cost list.
        return minCost[-1]

# Bottom-up Dynamic Programming (Constant Space)
class Solution:   
    def minCostClimbingStairs(self, cost):
        # Initialize the minimum cost to reach one step below the current step as 0
        one = 0
        # Initialize the minimum cost to reach two steps below the current step as 0
        two = 0
        # Start iterating from the 2nd stair (index 2) because the minimum cost to reach the first two stairs (index 0 and 1) is already known.
        for i in range(2, len(cost) + 1):
            # Save the temporary minimum cost to reach one step below the current step
            temp = one
            # Calculate the minimum cost for the current step by comparing the cost of taking a single step from the previous stair or a two-step jump from two stairs back
            one = min(one + cost[i-1], two + cost[i-2])
            # Update the minimum cost to reach two steps below the current step using the previously saved temporary minimum cost
            two = temp
        # Return the minimum cost to reach the top of the stairs
        return one

    
# Top-Down Dynamic Programming (Recursion and Memoization)
class Solution:
    def minCostClimbingStairs(self, cost):
        # Define a dictionary 'minCostDict' to store the minimum cost to reach each stair.
        # The keys are stair indices, and values are the corresponding minimum costs.
        minCostDict = {}

        # Define a helper function 'minCost' that calculates the minimum cost to reach a given stair 'i'.
        def minCost(i):
            # If the stair index 'i' is 0 or 1, the cost is 0, as we can start from either of the first two stairs.
            if i <= 1:
                return 0

            # If the minimum cost for stair 'i' is already calculated, return it from 'minCostDict'.
            if i in minCostDict:
                return minCostDict[i]

            # Otherwise, calculate the minimum cost recursively using the formula:
            # cost to reach 'i' = min(cost of 'i-1' + cost to reach 'i-1', cost of 'i-2' + cost to reach 'i-2').
            minCostDict[i] = min(cost[i-1] + minCost(i-1),
                                 cost[i-2] + minCost(i-2))

            # Return the calculated minimum cost for stair 'i'.
            return minCostDict[i]

        # Return the minimum cost to reach the top of the staircase.
        # The top is considered to be one step beyond the last step, hence the length of the 'cost' array.
        return minCost(len(cost))
