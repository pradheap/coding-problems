
def buy_and_sell(prices):
    if len(prices) == 0:
        return 0

    # The leastest profit.
    max_profit = 0
    # The minimum so far should be large 
    min_so_far = float("inf")
    for price in prices:
        max_profit = max(max_profit, price - min_so_far)
        min_so_far = min(min_so_far, price)
    return max_profit
