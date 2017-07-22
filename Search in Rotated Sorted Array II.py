def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """

    l, r = 0, len(nums) - 1

    while l <= r:
        print l, r

        mid = (l + r) / 2

        print nums[mid]
        if nums[mid] == target:
            return True

        while l < mid and nums[l] == nums[mid]:
            l += 1

        print l, r
        if nums[l] == target or nums[r] == target:
            return True
        else:
            if nums[l] <= nums[mid]:
                if nums[l] < target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

    return False


if __name__ == '__main__':
    print search([1,1,3,1], 3)