def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # ##############
    # # Solution 1
    #
    # n = len(nums)
    # if n == 1 and nums[0] >= 0:
    #     return True
    #
    # dp = []
    # for i in range(n):
    #     dp.append(0)
    #
    # stack = [0]
    # new_stack = []
    #
    # while True:
    #     if len(stack) == 0:
    #         stack = new_stack
    #         new_stack = []
    #         if len(stack) == 0:
    #             return False
    #     idx = stack.pop(0)
    #     for i in range(nums[idx]-1, -1, -1):
    #         if idx + i + 1 >= n - 1:
    #             return True
    #         if dp[idx + i + 1] == 0:
    #             dp[idx + i + 1] = 1
    #             new_stack.append(idx + i + 1)

    ##############
    # Solution 2

    n = len(nums)

    i = 0
    reach = 0

    while i < n and i <= reach:
        reach = max(reach, i + nums[i])
        i += 1

    return i == n

if __name__ == '__main__':
    print jump([3,2,1,0,4])