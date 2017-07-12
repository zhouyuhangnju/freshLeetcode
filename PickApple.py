def pick_apple(m, n, table):

    if m == 0 or n == 0:
        return 0

    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            dp[i][j] = table[i][j]
            prei, prej = 0, 0
            if i >= 1:
                prei= dp[i-1][j]
            if j >= 1:
                prej = dp[i][j-1]
            dp[i][j] += max(prei, prej)

    print dp

    return dp[m-1][n-1]


if __name__ == '__main__':
    print pick_apple(3, 4, [[1,2,9,10],[5,6,4,3], [2, 8, 7, 6]])