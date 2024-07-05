def maxProfit(prices):
    minPrice = float("inf")
    maxProfit = -1

    for price in prices:
        minPrice = min(minPrice, price)
        maxProfit = max(maxProfit, (price - minPrice))
    
    return maxProfit

if __name__ == "__main__":
    arr = [7,1,5,3,6,4]
    result = maxProfit(arr)
    print(result)
