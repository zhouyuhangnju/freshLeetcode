def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """

    if m == 0 or n == 0:
        return 0

    dp = [[0] * n for _ in range(m)]

    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]

    print dp

    return dp[m-1][n-1]


if __name__ == '__main__':
    print uniquePaths(3, 7)