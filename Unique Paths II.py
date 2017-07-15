def uniquePathsWithObstacles(obstacleGrid):
    """
    :type m: int
    :type n: int
    :rtype: int
    """

    m = len(obstacleGrid)
    if m == 0:
        return 0
    n = len(obstacleGrid[0])
    if n == 0:
        return 0

    if obstacleGrid[0][0] == 1:
        return 0

    dp = [[0] * n for _ in range(m)]

    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]

    print dp

    return dp[m-1][n-1]


if __name__ == '__main__':
    print uniquePathsWithObstacles([
  [0,0,1],
  [0,1,0],
  [0,0,0]
])