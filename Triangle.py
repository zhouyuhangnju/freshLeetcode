def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """

    n = len(triangle)

    if n <= 0:
        return 0

    minisum = triangle[0]

    for i in range(1, n):
        currminisum = []

        currminisum.append(triangle[i][0] + minisum[0])

        for j in range(1, i):
            currminisum.append(triangle[i][j] + min(minisum[j-1], minisum[j]))

        currminisum.append(triangle[i][i] + minisum[i-1])

        minisum = currminisum

    return min(minisum)


if __name__ == '__main__':
    print minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])