"""
Joe’s code problem on November 18th, 2023

Title: 121. Best Time to Buy and Sell Stock
Tag: Array, Dynamic Programming
Difficulty: Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
	# We initialize the minimum price to positive infinity.
        minPrice = float('inf')
        # We set maximum profit to 0.
        maxProfit = 0
        # As we iterate over the prices list, we encounter two scenarios:
        for i in range(len(prices)):
            # Scenario A: If the current price is less than the minimum price, we should update the minimum price to the current price. However, in this scenario, we cannot generate a profit here.
            if prices[i] < minPrice:
                minPrice = prices[i]
            # If the current price is higher than or equal to the minimum price, there is potential for making a profit. Moreover, if the difference between the current price and the minimum price exceeds the current maximum profit, we should update the maximum profit to this new difference.
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
        # By the end of the iteration, we return the maximum profit.
        return maxProfit

            
        