def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """

    # solution is similar with 'Container with Most Water'

    l, r = 0, len(height) - 1
    maxl, maxr = 0, 0

    res = 0
    while l < r:
        if height[l] < height[r]:
            if height[l] > maxl:
                maxl = height[l]
            else:
                res += (maxl - height[l])
            l += 1
        else:
            if height[r] > maxr:
                maxr = height[r]
            else:
                res += (maxr - height[r])
            r -= 1

    return res

if __name__ == '__main__':
    print trap([0,1,0,2,1,0,1,3,2,1,2,1])