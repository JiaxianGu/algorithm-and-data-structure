def maxProfit(prices):
    if len(prices) <= 0:
        return 0
    lowest = prices[0]
    max_profit = [0] * len(prices)
    max_profit[0] = 0
    for i in range(1, len(prices)):
        max_profit[i] = max(max_profit[i-1], prices[i] - lowest)
        if prices[i] <= lowest:
            lowest = prices[i]
    return max_profit[len(prices)-1]
    