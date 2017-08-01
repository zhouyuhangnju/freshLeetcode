def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    buyprice = 2**31-1

    profit = 0
    for i in range(len(prices)):
        buyprice = min(buyprice, prices[i])
        profit = max(profit, prices[i] - buyprice)

    return profit

if __name__ == '__main__':
    print maxProfit([7, 1, 5, 3, 6, 4])