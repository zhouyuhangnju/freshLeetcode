def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    max = -2147483647

    curr_sum = 0
    for n in nums:
        curr_sum += n
        if curr_sum > max:
            max = curr_sum
        if curr_sum < 0:
            curr_sum = 0

    return max


if __name__ == '__main__':
    print maxSubArray([-2147483647])