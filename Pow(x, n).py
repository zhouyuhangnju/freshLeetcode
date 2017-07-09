def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """

    if x == 0:
        return 0
    if n == 0:
        return 1

    mid = int(float(n) / 2)
    midpow = myPow(x, mid)
    if mid == n - mid:
        return midpow * midpow
    else:
        if n > 0:
            return x * midpow * midpow
        else:
            return 1 / x * midpow * midpow


if __name__ == '__main__':
    print myPow(-0.5, 3)
