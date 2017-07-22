def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if len(nums) == 0:
        return 0

    newlen = 0

    count = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[newlen]:
            newlen += 1
            nums[newlen] = nums[i]
            count = 1
        else:
            if count < 2:
                newlen += 1
                nums[newlen] = nums[i]
                count = 2

    return newlen + 1


if __name__ == '__main__':
    a = [1,1,1,2,2,3]
    print removeDuplicates(a)
    print a