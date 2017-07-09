def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    if len(nums) == 0:
        return []

    i = len(nums) - 1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1

    if i != 0:
        j = len(nums) - 1
        while j > i and nums[i-1] >= nums[j]:
            j -= 1

        nums[i-1], nums[j] = nums[j], nums[i-1]

    k = len(nums) - 1
    while i < k:
        nums[i], nums[k] = nums[k], nums[i]
        i += 1
        k -= 1

    return nums

if __name__ == '__main__':
    print nextPermutation([5,1,1])