def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """

    if x < 0:
        return -1

    def binarySearch(i, j):
        if j < i:
            return min(i, j)

        mid = (i + j) / 2
        res = mid * mid
        if res == x:
            return mid
        elif res > x:
            return binarySearch(i, mid-1)
        else:
            return binarySearch(mid+1, j)

    return binarySearch(0, x)


if __name__ == '__main__':
    print mySqrt(10)