def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """

    dp = [0] * n

    dp[0] = 1

    if n > 1:

        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

    return dp[n-1]


if __name__ == '__main__':
    print climbStairs(2)