def numTrees(n):
    """
    :type n: int
    :rtype: int
    """

    dp = [1] * (n + 1)

    for i in range(1, n + 1):
        res = 0
        for j in range(1, i+1):
            res += dp[j-1] * dp[i-j]
        dp[i] = res

    dp[0] = 0
    return dp[n]


if __name__ == '__main__':
    print numTrees(4)