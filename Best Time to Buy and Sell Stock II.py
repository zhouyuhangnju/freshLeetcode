def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    if len(prices) <= 0:
        return 0

    profit = 0

    buyprice = -1
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i] and buyprice == -1:
            buyprice = prices[i]
        elif prices[i+1] < prices[i] and buyprice >= 0:
            assert buyprice <= prices[i]
            profit += prices[i] - buyprice
            buyprice = -1

    if prices[-1] > buyprice and buyprice >= 0:
        profit += prices[-1] - buyprice

    return profit


if __name__ == '__main__':
    print maxProfit([1,2,4,2,5,7,2,4,9,0])