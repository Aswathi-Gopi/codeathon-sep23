def find_max_profit(prices):
    if len(prices) < 2:
        return -1

    buy_day = 0
    sell_day = 1
    max_profit = prices[sell_day] - prices[buy_day]

    for i in range(1, len(prices)):
        if prices[i] < prices[buy_day]:
            buy_day = i
            sell_day = i + 1
        elif prices[i] > prices[sell_day]:
            sell_day = i
        if prices[sell_day] - prices[buy_day] > max_profit:
            max_profit = prices[sell_day] - prices[buy_day]

    if max_profit <= 0:
        return -1

    return (buy_day + 1, prices[buy_day], sell_day + 1, prices[sell_day], max_profit)
