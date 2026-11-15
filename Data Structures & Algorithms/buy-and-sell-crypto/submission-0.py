class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        for i in range(len(prices)):
            for v in range(i + 1, len(prices)):
                prof = max( prices[v] - prices[i], prof)
        return prof