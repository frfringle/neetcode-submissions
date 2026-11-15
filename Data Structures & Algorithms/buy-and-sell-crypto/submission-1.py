class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        l = 0
        r = 1
        while l < r and r < len(prices):
            if prices[r] > prices[l]:
                # take profits
                prof = max(prices[r] - prices[l], prof)
                
            else:
                # if the next value is cheaper than current value, thats the better buy day
                l=r
            r+= 1

        return prof