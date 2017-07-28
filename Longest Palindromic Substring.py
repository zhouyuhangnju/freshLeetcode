def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    n = len(s)

    if n <= 0:
        return ''

    dp = [[False] * n for _ in range(n)]

    for j in range(n):
        dp[0][j] = True

    maxlen = 0
    for i in range(1, n):
        flag = False
        for j in range(n-i):
            dp[i][j] = s[j] == s[j+i]
            if j+1 <= j+i-1:
                dp[i][j] = dp[i][j] and dp[i-2][j+1]
            if dp[i][j] == True:
                flag = True
        if flag:
            maxlen = i

    print dp
    print maxlen
    for j in range(n-maxlen):
        if dp[maxlen][j]:
            return s[j:j+maxlen+1]

    return ''






if __name__ == '__main__':
    print longestPalindrome("cbbd")
