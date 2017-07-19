def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    def subsearch(array, i, j):
        if i > j:
            return j, 0
        mid = (i + j) / 2
        if mid >= len(array):
            return mid - 1, 0
        if array[mid] == target:
            return mid, 1
        elif array[mid] < target:
            return subsearch(array, mid+1, j)
        else:
            return subsearch(array, i, mid-1)

    def searchrow():
        return subsearch([row[0] for row in matrix], 0, len(matrix))

    def searchcol(row):
        _, flag = subsearch(matrix[row], 0, len(matrix[row]))
        return flag == 1

    if len(matrix) == 0:
        return False
    if len(matrix[0]) == 0:
        return False

    row, flag = searchrow()
    if flag == 1:
        return True
    if row < 0:
        return False
    else:
        return searchcol(row)

if __name__ == '__main__':
    print searchMatrix([[1,3]], 3)