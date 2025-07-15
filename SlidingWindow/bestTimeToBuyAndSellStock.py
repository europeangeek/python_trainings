from typing import List, Tuple

class Solution:
    """
    You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

    You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

    Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
    
    Another variation might be the amount of days to hold before selling thats why the problem is sligly modified with an output (tuple with maxProfit and amount of days)
    """
    def maxProfit(self, prices: List[int]) -> Tuple[int, int]:
        l: int = 0
        r: int = 1
        maxProfit = 0
        days = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                if profit > maxProfit:
                    maxProfit = profit
                    days = r - l
            r += 1
        return (maxProfit, days)
                
    

prices = [10, 2, 5, 6, 7, 8]
s = Solution()
print(s.maxProfit(prices))
