"""
Joe’s code problem on November 19th, 2023

Title: 122. Best Time to Buy and Sell Stock II
Tag: Array, Dynamic Programming, Greedy
Difficulty: Medium

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 
Constraints:
1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
    
"""

class Solution:
    def maxProfit(self, prices):
	    # We set cumulative profit to 0.
        cumulativeProfit = 0
        # We iterate over the price list using two adjacent pointers, i and i+1.
        for i in range(len(prices)-1):
            # If the later price is higher than the previous price, a profit can be made from this trade. 
            if prices[i+1] > prices[i]:
                # In this case, we add the difference between the later price and the previous price to the cumulative profit.
                cumulativeProfit += prices[i+1] - prices[i]
        # By the end of the iteration, we return the cumulative profit.
        return cumulativeProfit
