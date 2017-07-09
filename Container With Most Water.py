def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """

    # return max([min(height[i], height[i+1]) for i in range(len(height)-1)])

    maxvol = 0
    i, j = 0, len(height) - 1

    while i < j:
        maxvol = max(maxvol, (j - i) * min(height[i], height[j]))

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return maxvol

if __name__ == '__main__':
    print maxArea([3,2,1,3])