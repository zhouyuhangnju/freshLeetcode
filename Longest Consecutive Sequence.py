def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    maxlen = 0

    nums = set(nums)

    for n in nums:
        if n-1 not in nums:
            y = n + 1
            while y in nums:
                y += 1
            maxlen = max(maxlen, y - n)

    return maxlen

if __name__ == '__main__':
    print longestConsecutive([100, 4, 200, 1, 3, 2])