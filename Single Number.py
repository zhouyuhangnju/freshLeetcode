def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    res = 0

    for n in nums:
        res = res ^ n

    return res


if __name__ == '__main__':
    print singleNumber([1,2,2,3])