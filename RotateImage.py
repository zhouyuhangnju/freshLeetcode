def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """

    n = len(matrix)

    mid = n / 2

    for i in range(mid):
        for j in range(n - 2 * i - 1):
            print i, j
            tmp = matrix[i][i+j]
            matrix[i][i+j] = matrix[n - i - 1 - j][i]
            matrix[n - i - 1 - j][i] = matrix[n - i - 1][n - i - 1 - j]
            matrix[n - i - 1][n - i - 1 - j] = matrix[i + j][n - i - 1]
            matrix[i + j][n - i - 1] = tmp

if __name__ == '__main__':
    matrix = [[1]]
    rotate(matrix)

    print matrix