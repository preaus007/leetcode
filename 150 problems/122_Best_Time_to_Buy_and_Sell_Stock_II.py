def maxProfit(prices):
    totalProfit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            totalProfit += prices[i] - prices[i - 1]
    return totalProfit

if __name__ == "__main__":
    arr = [7,1,5,3,6,4]
    result = maxProfit(arr)
    print(result)
