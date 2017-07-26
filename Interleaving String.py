def isInterleave(s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """

    l1, l2 = len(s1), len(s2)

    if l1 + l2 != len(s3):
        return False

    dp = [[False] * (l2+1) for _ in range(l1+1)]

    dp[0][0] = True
    for i in range(1, l1+1):
        dp[i][0] = s1[:i] == s3[:i]

    for j in range(1, l2+1):
        dp[0][j] = s2[:j] == s3[:j]

    for i in range(1, l1+1):
        for j in range(1, l2+1):
            flag = False
            if s1[i - 1] == s3[i + j - 1]:
                flag = dp[i - 1][j] or flag
            if s2[j - 1] == s3[i + j - 1]:
                flag = dp[i][j - 1] or flag
            dp[i][j] = flag

    return dp[l1][l2]


if __name__ == '__main__':
    print isInterleave("a", "a", "a")