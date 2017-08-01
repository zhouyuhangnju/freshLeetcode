def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """

    slen, tlen = len(s), len(t)

    if tlen > slen:
        return 0

    dp = [[0] * slen for _ in range(tlen)]

    for i in range(tlen):
        for j in range(i, slen):
            print s[j], t[i]
            if j > 0:
                dp[i][j] += dp[i][j-1]
            if s[j] == t[i]:
                if i == 0:
                    dp[i][j] += 1
                elif i > 0 and j > 0:
                    dp[i][j] += dp[i-1][j-1]

    print dp

    return dp[tlen-1][slen-1]


if __name__ == '__main__':
    print numDistinct("ddd", "dd")