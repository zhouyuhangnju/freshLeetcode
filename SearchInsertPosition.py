def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    if len(nums) == 0:
        return 0

    l, r = 0, len(nums) - 1

    while l <= r:

        mid = (l + r) / 2

        if target == nums[mid]:
            return mid

        if target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1

    if l != r:
        return max(l, r)
    else:
        if target > nums[l]:
            return l + 1
        else:
            return l - 1



if __name__ == '__main__':
    print searchInsert([1,3,5,6], 7)