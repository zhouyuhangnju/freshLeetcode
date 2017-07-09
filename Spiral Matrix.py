def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """

    res = []

    m = len(matrix)

    if m == 0:
        return []

    n = len(matrix[0])

    ends = [n, m, -1, 0]

    currloc = [0, -1]

    while True:

        if currloc[1] == ends[0] - 1:
            break
        else:
            while currloc[1] < ends[0] - 1:
                currloc[1] += 1
                print currloc
                res.append(matrix[currloc[0]][currloc[1]])
            ends[0] -= 1

        if currloc[0] == ends[1] - 1:
            break
        else:
            while currloc[0] < ends[1] - 1:
                currloc[0] += 1
                print currloc
                res.append(matrix[currloc[0]][currloc[1]])
            ends[1] -= 1

        if currloc[1] == ends[2] + 1:
            break
        else:
            while currloc[1] > ends[2] + 1:
                currloc[1] -= 1
                print currloc
                res.append(matrix[currloc[0]][currloc[1]])
            ends[2] += 1

        if currloc[0] == ends[3] + 1:
            break
        else:
            while currloc[0] > ends[3] + 1:
                currloc[0] -= 1
                print currloc
                res.append(matrix[currloc[0]][currloc[1]])
            ends[3] += 1

    return res



if __name__ == '__main__':
    print spiralOrder([])