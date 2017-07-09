def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """

    res = [[0] * n for _ in range(n)]

    loc = [0, 0]
    orientation = 0

    for i in range(n * n):

        res[loc[0]][loc[1]] = i + 1

        if orientation == 0:
            loc[1] += 1
            if loc[1] == n or res[loc[0]][loc[1]] != 0:
                loc[1] -= 1
                loc[0] += 1
                orientation = 1
        elif orientation == 1:
            loc[0] += 1
            if loc[0] == n or res[loc[0]][loc[1]] != 0:
                loc[0] -= 1
                loc[1] -= 1
                orientation = 2
        elif orientation == 2:
            loc[1] -= 1
            if loc[1] == -1 or res[loc[0]][loc[1]] != 0:
                loc[1] += 1
                loc[0] -= 1
                orientation = 3
        elif orientation == 3:
            loc[0] -= 1
            if res[loc[0]][loc[1]] != 0:
                loc[0] += 1
                loc[1] += 1
                orientation = 0

    return res



if __name__ == '__main__':
    print generateMatrix(5)