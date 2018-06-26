def get_max_profit(stock_prices):
    # Calculate the max profit
    m = stock_prices[0]
    mp = stock_prices[1] - stock_prices[0]

    for i in range(0, len(stock_prices)):
        c = stock_prices[i]
        p = c - m
        mp = max(mp, p)
        m = min(m, c)

    return mp

li=[1,2,3,9]
print(get_max_profit(li))