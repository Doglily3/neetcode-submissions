class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        maxdiff = 0
        for i in range(length-1):
            for j in range(i, length):
                 diff = prices[j] - prices[i]
                 maxdiff = max(maxdiff,diff)
        return maxdiff