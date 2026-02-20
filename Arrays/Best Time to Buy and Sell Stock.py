"""
Day 2 - DSA Journey (LeetCode)

Problem: Best Time to Buy and Sell Stock
LeetCode No: 121
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Date: 20-02-2026
Language: Python

----------------------------------------
Problem Faced During Practice:
----------------------------------------
While solving this problem, I initially tried a brute force approach
by comparing all possible pairs of buying and selling days using
nested loops.

However, this caused two major logical mistakes:

1. I was comparing any two days without ensuring that the buying
   day comes before the selling day.

2. In some cases, my logic was allowing buying on a future day
   and selling on a past day, which violates the real-world
   constraint of stock trading.

Example:
prices = [5,1]

My Wrong Logic:
buy = 1
sell = 5
profit = 4

Expected Output:
0

Reason:
The logic selected the minimum and maximum values from any
two days without checking the time order. This effectively
allowed buying in the future and selling in the past.

----------------------------------------
Initial Approach (Brute Force - Wrong Logic)
----------------------------------------

for i in range(len(prices)):
    for j in range(i+1, len(prices)):
        buy = min(prices[i], prices[j])
        sell = max(prices[i], prices[j])
        return sell - buy

Time Complexity: O(n^2)
Space Complexity: O(1)

----------------------------------------
Optimized Approach (Greedy - Correct Logic)
----------------------------------------
Instead of checking all possible pairs of days, I realized that
I need to track the minimum price seen so far as the best buying
day and calculate the profit dynamically for each day.

For every day:
Profit = Today's Price - Minimum Price Seen So Far

If the current price is less than the previous minimum,
update the buying day.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution(object):
    def maxProfit(self, prices):
        i = 0
        j = 1
        max_profit = 0

        while j < len(prices):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]

            if prices[j] < prices[i]:
                i = j

            j += 1

        return max_profit
