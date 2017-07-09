import numpy as np

def isMatch(s, p):


    dp = np.zeros((len(s) + 1, len(p) + 1))

    dp[0][0] = 1

    for i in range(1, len(p) + 1):
        if p[i - 1] == '*':
            dp[0][i] = 1
        else:
            break

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            else:
                if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

    return True if dp[len(s)][len(p)] == 1 else False



if __name__ == '__main__':
    print isMatch("ab", "?*")