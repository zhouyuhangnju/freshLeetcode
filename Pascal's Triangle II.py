def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """

    res = []
    if numRows <= 0:
        return res

    res = [1]

    for i in range(1, numRows):
        currres = []

        currres.append(1)
        for j in range(len(res)-1):
            currres.append(res[j]+res[j+1])
        currres.append(1)

        res = currres

    return res


if __name__ == '__main__':
    print generate(3)