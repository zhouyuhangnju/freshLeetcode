def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """

    res = []
    if numRows <= 0:
        return res

    res.append([1])
    for i in range(1, numRows):
        preres = res[-1]
        currres = []

        currres.append(1)
        for j in range(len(preres)-1):
            currres.append(preres[j]+preres[j+1])
        currres.append(1)

        res.append(currres)

    return res


if __name__ == '__main__':
    print generate(5)