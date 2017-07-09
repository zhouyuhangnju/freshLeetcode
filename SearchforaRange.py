def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    res = [-1, -1]

    l, r = 0, len(nums) - 1

    while l <= r:

        mid = (l + r) / 2

        if target == nums[mid]:
            i, j = mid, mid
            while i >= l and target == nums[i]:
                i -= 1
            res[0] = i + 1
            while j <= r and target == nums[j]:
                j += 1
            res[1] = j - 1
            return res
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1

    return res


if __name__ == '__main__':
    print searchRange([5, 7, 7, 8, 8, 10], 8)