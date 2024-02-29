class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        buy = 0
        prft = 0

        for sell in range(1, len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                prft = max(prft, profit)

        return prft
