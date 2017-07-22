def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """

    def subLargestRectangleArea(start, end):

        if start == end:
            return heights[start]

        mid = (start + end) / 2
        maxArea = max(combineRectangleArea(start, end, mid), subLargestRectangleArea(start, mid), subLargestRectangleArea(mid+1, end))

        return maxArea

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
                if heights[i-1] >= heights[j+1]:
                    i -= 1
                else:
                    j += 1

        return maxArea

    if len(heights) == 0:
        return 0
    return subLargestRectangleArea(0, len(heights) - 1)







if __name__ == '__main__':
    print largestRectangleArea([4,2,0,3,2,4,3,4])