"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

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

1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            # If today's price is more than yesterday's, take the profit
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
"""
✅ Time and Space Complexity
Metric	          Value
Time Complexity	   O(n)
Space Complexity   O(1)
"""
"""
🔹 Line 1:

for i in range(1, len(prices)):
What it means:
We’re using a for loop to look at each day starting from index 1 (second element).
Why start from 1? Because we want to compare 
today’s price with yesterday’s price — and prices[i - 1] would be invalid if i = 0.

🧠 Real Example:
Let’s say:

prices = [1, 5, 3, 6]
Then:

i = 1: compare prices[1] = 5 with prices[0] = 1

i = 2: compare prices[2] = 3 with prices[1] = 5

i = 3: compare prices[3] = 6 with prices[2] = 3

We loop through these pairs one by one.

🔹 Line 2:

if prices[i] > prices[i - 1]:
What it means:
Check if today's price is higher than yesterday’s.
If yes → we could’ve bought yesterday and sold today to make a profit.
So, we’ll add that profit.

🔹 Line 3:

profit += prices[i] - prices[i - 1]
What it means:
We calculate the profit for today:
today’s price
−
yesterday’s price
today’s price−yesterday’s price
And add that to our total profit.

🧠 If today’s price is not more than yesterday’s, we just skip (do nothing).

🔹 Final Line:

return profit
After the loop is done checking all days,

We return the total profit we collected from all the small increases.

📌 Full Example Walkthrough

prices = [1, 5, 3, 6]
Let’s go through the loop:

i	prices[i-1]	prices[i]	Is i > i-1?	Profit Added	Total Profit
1	1	         5	         Yes	       5 - 1 = 4	4
2	5	         3	         No	           0	        4
3	3	         6	          Yes	       6 - 3 = 3	7

✅ Final Output: 7

"""