prices = [7,1,5,3,6,4]
# prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]

def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        # If today's price is higher than yesterday's, take the profit
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

print(maxProfit(prices))