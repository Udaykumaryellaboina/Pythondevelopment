"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a 
different day in the future to sell that stock.

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

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initialize with a very large number
        max_profit = 0            # Initialize profit as 0

        for price in prices:
            if price < min_price:
                min_price = price  # Found a new lower price — better to buy here
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Found better profit if sold today

        return max_profit


"""
✅ Time and Space Complexity
Time: O(n) → One pass through the array

Space: O(1) → Only two variables used
"""

#🧠 Problem (In Simple Words)
"""You are given the stock prices for n days in a list, like this:

prices = [7, 1, 5, 3, 6, 4]
Each value in the list is the price of a stock on that day:

Day 0 → price = 7
Day 1 → price = 1
Day 2 → price = 5
Day 3 → price = 3
Day 4 → price = 6
Day 5 → price = 4

You need to buy the stock on one day and sell it on a later day, and make the maximum profit.
You cannot sell before you buy.

✅ Goal:
Find out the best day to buy and the best day to sell after that, such that:

profit = sell_price - buy_price
And return the maximum possible profit. If no profit is possible, return 0.

✅ Real-World Example
Imagine you’re watching gold prices for 6 days:

Day	Price
0	₹7
1	₹1 ✅ lowest price (buy here)
2	₹5
3	₹3
4	₹6 ✅ highest after buying at ₹1
5	₹4

If you buy on day 1 at ₹1, and sell on day 4 at ₹6 → Profit = ₹5.
This is the best deal, so the answer is 5.



Day	Price	min_price	price - min_price	 max_profit  	Explanation
0	7	    7	         -	                  0	              First price, set min_price to 7
1	1	    1 ✅	     -	                  0             	New lowest, update min_price to 1
2	5	    1	         4 ✅	              4             	Profit = 5 - 1 = 4 → update max_profit
3	3	    1	         2	                  4	                Profit = 3 - 1 = 2 < 4 → no update
4	6	    1	         5 ✅	              5 ✅	            Best profit → update max_profit to 5
5	4	    1            3	                  5	                Less than 5 → no update

Final answer: 5

✅ Line-by-Line Explanation
def maxProfit(prices):  # Function that takes a list of prices

min_price = float('inf')  # Start with very high value
This means we haven't seen any price yet.
Any real price will be lower than this.

max_profit = 0
Start with 0 profit, because no transaction is done yet.


    for price in prices:
Loop through each day’s price.

        if price < min_price:
            min_price = price
If current price is lower than previous lowest → update min_price

This is like saying: "Hey! This is a better day to buy!"


        elif price - min_price > max_profit:
            max_profit = price - min_price
Else, check: "If I sell today, how much profit do I make?"

If it's better than previous best → update max_profit.

    return max_profit
After checking all days, return the highest profit we found.

🎯 Key Idea:
Always look for the lowest price to buy and highest price to sell after it.

You're only looping once through the list → Time Complexity = O(n) (very efficient)"""