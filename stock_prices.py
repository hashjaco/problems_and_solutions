from typing import List

"""
>>> max_trade_profit([2, 1, 0])
0
>>> max_trade_profit([1, 23, 4, 12, 13, 56])
55
>>> max_trade_profit([43, 15, 45, 34, 3, 14, 19])
30
"""

def max_trade_profit(prices: List[int]) -> int:
    if not prices:
        return 0

    buy_day, max_profit = 0, 0
    for curr_day, price in enumerate(prices, 1):
        sell_profit = price - prices[buy_day]
        if price < prices[buy_day]:
            buy_day = curr_day
        elif sell_profit > max_profit:
            max_profit = sell_profit

        curr_day += 1
    return max_profit


print(max_trade_profit([2, 1, 0]))
print(max_trade_profit([1, 23, 4, 12, 13, 56]))
print(max_trade_profit([43, 15, 45, 34, 3, 14, 19]))
