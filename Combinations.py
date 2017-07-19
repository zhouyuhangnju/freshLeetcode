def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """

    res = []

    def subcombine(start, curr):
        if len(curr) == k:
            res.append(curr)
        else:
            for i in range(start, n):
                subcombine(i+1, curr + [i+1])

    if k <= n / 2:
        subcombine(0, [])
    else:
        k = n - k
        subcombine(0, [])
        res = [list(set(range(1, n+1)) - set(r)) for r in res]

    return res


if __name__ == '__main__':
    res = combine(20, 16)
    print len(res)
    print res