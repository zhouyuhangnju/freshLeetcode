def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """

    m = len(matrix)

    if m == 0:
        return

    n = len(matrix[0])
    if n == 0:
        return

    rowflag = 0
    colflag = 0

    for i in range(m):
        if matrix[i][0] == 0:
            rowflag = 1
            break

    for i in range(n):
        if matrix[0][i] == 0:
            colflag = 1
            break

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    print matrix

    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0

    for i in range(1, n):
        if matrix[0][i] == 0:
            for j in range(1, m):
                matrix[j][i] = 0

    if rowflag == 1:
        for i in range(m):
            matrix[i][0] = 0

    if colflag == 1:
        for i in range(n):
            matrix[0][i] = 0



if __name__ == '__main__':
    A = [[3,5,5,6,9,1,4,5,0,5],[2,7,9,5,9,5,4,9,6,8],[6,0,7,8,1,0,1,6,8,1],[7,2,6,5,8,5,6,5,0,6],[2,3,3,1,0,4,6,5,3,5],[5,9,7,3,8,8,5,1,4,3],[2,4,7,9,9,8,4,7,3,7],[3,5,2,8,8,2,2,4,9,8]]

    setZeroes(A)

    print A