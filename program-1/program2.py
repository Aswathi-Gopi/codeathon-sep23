def find_max_profit(prices):
    """
    Finds the best days to buy and sell stocks to maximize profit, given an array of stock prices.
    Returns the maximum profit that can be made. If no profit can be made, returns -1.

    Args:
        prices (list): A list of stock prices.

    Returns:
        tuple: A tuple containing the buy day, buy price, sell day, sell price, and maximum profit.
               If no profit can be made, returns -1.
    """
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
