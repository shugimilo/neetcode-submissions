class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 100
        maxDiff = 0
        for i, price in enumerate(prices):
            if price < minPrice:
                minPrice = price
            if price - minPrice > maxDiff:
                maxDiff = price - minPrice

        return maxDiff