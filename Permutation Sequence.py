def getPermutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """

    a = [i+1 for i in range(n)]

    tmplist = []

    tmp = 1
    for j in range(1, n):
        tmp *= j
        tmplist.append(tmp)

    res = ''
    for j in range(n-1, 0, -1):
        print res
        print k, tmplist[j-1]
        d, m  = divmod(k, tmplist[j-1])
        if m == 0:
            res += str(a.pop(d-1))
            k -= tmplist[j - 1] * (d-1)
        else:
            res += str(a.pop(d))
            k -= tmplist[j-1] * d

    res += str(a[-1])

    return res



if __name__ == '__main__':
    print getPermutation(4, 24)