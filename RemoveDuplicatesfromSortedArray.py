def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if len(nums) == 0:
        return 0

    newlen = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[newlen]:
            newlen += 1
            nums[newlen] = nums[i]

    return newlen+1

if __name__ == '__main__':
    nums = [1,1,2,3,3,4,5,6,6,6]
    print removeDuplicates(nums)
    print nums