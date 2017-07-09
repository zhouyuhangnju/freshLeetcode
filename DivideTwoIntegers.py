def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """

    ispos = (dividend >= 0) == (divisor >= 0)
    dividend, divisor = abs(dividend), abs(divisor)

    res = 0
    while dividend >= divisor:
        a, b = divisor, 1
        while dividend >= a:
            dividend -= a
            res += b
            a <<= 1
            b <<= 1

    if not ispos:
        res = -res

    return max(min(res, 2 ** 31 - 1), - 2 ** 31)



if __name__ == '__main__':
    print divide(-2147483648, 1)