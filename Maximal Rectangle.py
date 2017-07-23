def maximalRectangle(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """

    def largestRectangleArea(heights):

        def combineRectangleArea(start, end, mid):

            i, j = mid, mid + 1
            h = min(heights[i], heights[j])
            maxArea = 0

            while i >= start and j <= end:
                h = min(h, min(heights[i], heights[j]))
                maxArea = max(maxArea, h * (j - i + 1))

                if i == start:
                    j += 1
                elif j == end:
                    i -= 1
                else:
                    if heights[i - 1] > heights[j + 1]:
                        i -= 1
                    else:
                        j += 1

            return maxArea

        def subLargestRectangleArea(start, end):

            if start == end:
                return heights[start]

            mid = (start + end) / 2

            return max(combineRectangleArea(start, end, mid), subLargestRectangleArea(start, mid),
                       subLargestRectangleArea(mid+1, end))

        return subLargestRectangleArea(0, len(heights) - 1)

    # print largestRectangleArea([4,2,0,3,2,4,3,4])

    if len(matrix) <= 0:
        return -1
    if len(matrix[0]) <= 0:
        return -1

    maxArea = 0
    currHeights = [0] * len(matrix[0])
    for i in range(len(matrix)):
        currHeights = [currHeights[j] + 1 if matrix[i][j] == '1' else 0 for j in range(len(matrix[i]))]
        maxArea = max(maxArea, largestRectangleArea(currHeights))

    return maxArea


if __name__ == '__main__':
    print maximalRectangle(["10100","10111","11111","10010"])