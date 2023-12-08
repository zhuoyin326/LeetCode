"""
Joe’s code problem on December 2nd, 2023

Title: 714. Best Time to Buy and Sell Stock with Transaction Fee
Tag: Array, Dynamic Programming, Greedy
Difficulty: Medium

You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee. 
Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
Note:
You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.

Example 1:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6

Constraints:
1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104

"""

# Dynamic Programming Code:
class Solution:
	def maxProfit(prices, fee):
		n = len(prices)
		cash = n*[0]
		stock = n*[0]
		stock[0] = -prices[0]
		for i in range(0, n-1):
			cash[i+1] = max(cash[i], stock[i] + prices[i+1] - fee)
			stock[i+1] = max(stock[i], cash[i] - prices[i+1])
		return cash[-1]

# Space-Optimized Dynamic Programming Code:
class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        cash = 0
        stock = -prices[0]
        for i in range(1, n):
            tempStock = stock
            stock = max(stock, cash - prices[i])
            cash = max(cash, stock + prices[i] - fee)
        return cash
