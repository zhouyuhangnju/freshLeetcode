def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    l, r = 0, len(nums) - 1

    while l <= r:

        mid = (l + r) / 2
        if target == nums[mid]:
            return mid

        # If nums[mid] and target are on the same side of nums[0], we just take nums[mid].\
        # Otherwise we use - infinity or +infinity as needed.

        if nums[mid] == nums[0]:
            l = mid + 1
            continue

        if target == nums[0]:
            return 0

        if (nums[mid] - nums[0]) * (target - nums[0]) > 0:
            num = nums[mid]
        else:
            num = - 2 ** 31 if nums[mid] > nums[0] else 2 ** 31 - 1

        if target > num:
            l = mid + 1
        else:
            r = mid - 1

    return -1



if __name__ == '__main__':
    print search([5,1,3], 5)