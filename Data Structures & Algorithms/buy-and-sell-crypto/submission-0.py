class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 1
        j = 0
        while i < len(prices):
            sell = prices[i]
            while j < i:
                buy = prices[j]
                if sell - buy > profit:  
                    profit = sell - buy
                j = j + 1
            j = 0  
            i = i + 1
        return profit