
# method 1

def max_profit(prices):
    if not prices:
        return 0

    min_price = float('inf')
    print(min_price)
    max_profit = 0


    for price in prices:
        min_price = min(min_price, price)
        current_profit = price - min_price
        print(current_profit)
        max_profit = max(max_profit, current_profit)
        # print(max_profit)

    return max_profit


# method 2  [EASY ONE]

def max_profit2(prices):
    min_price = prices[0]
    profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > profit:
            profit = price - min_price
    
    return profit

prices = [7, 1, 5, 3, 6, 4]
result = max_profit2(prices)
print(f"The maximum profit is: {result}")
