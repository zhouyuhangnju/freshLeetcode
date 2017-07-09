def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    i = 0
    while i < len(nums):
        target = nums[i]
        if target < len(nums) and target > 0:
            if nums[target-1] != target:
                nums[target-1], nums[i] = nums[i], nums[target-1]
                i -= 1
        i += 1
    print nums

    for i in range(len(nums)):
        if i+1 != nums[i]:
            return i+1

    return len(nums)+1



if __name__ == '__main__':
    print firstMissingPositive([4,2,3,1])