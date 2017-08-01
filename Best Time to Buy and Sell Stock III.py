def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    if len(prices) <= 0:
        return 0

    flag = True
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            flag = False
    if flag:
        return 0

    K = 4

    dp = [[0] * len(prices) for _ in range(K)]

    for i in range(K):
        dp[i][0] = 0

    profit = 0
    buyprice = 2**31-1
    for j in range(len(prices)):
        buyprice = min(buyprice, prices[j])
        profit = max(profit, prices[j] - buyprice)
        dp[0][j] = profit

    for i in range(1, K):
        for j in range(1, len(prices)):
            for k in range(1, j-1):
                dp[i][j] = max(dp[i][j], dp[i-1][k] + prices[j] - prices[k+1])
            dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i][j])

    print dp
    return dp[-1][-1]


if __name__ == '__main__':
    print maxProfit([3,2,1,0,0,0])