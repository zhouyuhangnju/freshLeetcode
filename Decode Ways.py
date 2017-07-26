def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """

    if len(s) == 0 or s[0] == '0':
        return 0

    utillist = ['1', '2', '3', '4', '5', '6']

    dp = [0] * (len(s) + 1)

    dp[0], dp[1] = 1, 1

    for i in range(2, len(s) + 1):
        if (s[i-2] != '1' and s[i-2] != '2') and s[i-1] == '0':
            return 0
        if s[i - 2] == '1':
            if s[i-1] == '0':
                dp[i] = dp[i - 2]
            else:
                if i < len(s) and s[i] == '0':
                    dp[i] = dp[i - 1]
                else:
                    dp[i] = dp[i-1] + dp[i-2]
        elif s[i - 2] == '2':
            if s[i - 1] == '0':
                dp[i] = dp[i - 2]
            elif s[i-1] in utillist:
                if i < len(s) and s[i] == '0':
                    dp[i] = dp[i - 1]
                else:
                    dp[i] = dp[i - 1] + dp[i-2]
            else:
                dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1]

    print dp
    return dp[len(s)]



if __name__ == '__main__':
    print numDecodings('1010')