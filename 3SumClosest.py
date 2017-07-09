def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    maxdiff = 2**31-1

    nums = sorted(nums)
    print nums

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1

        while l < r:
            # print i, l, r
            s = nums[i] + nums[l] + nums[r]
            diff = s - target
            if diff < 0:
                diff = -diff

            # print diff, maxdiff
            if diff < maxdiff:
                result = s
                maxdiff = diff

            if s >= target + maxdiff:
                r -= 1
            elif s <= target - maxdiff:
                l += 1
            elif s > target and s < target + maxdiff:
                l += 1
            elif s < target and s > target - maxdiff:
                r -= 1
            else:
                assert s == target
                return target

    return result


if __name__ == '__main__':
    print threeSumClosest([0,2,1,-3], 1)
