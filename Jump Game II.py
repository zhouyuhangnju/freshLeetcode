def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # ##############
    # # Solution 1
    #
    # n = len(nums)
    #
    # dp = []
    # for i in range(n):
    #     dp.append([])
    #     for j in range(n):
    #         dp[i].append(n-1)
    #
    # for i in range(1, n):
    #     for j in range(n-i):
    #         if i == 1:
    #             if nums[j] > 0:
    #                 dp[j][j+i] = 1
    #         else:
    #             if nums[j] >= i:
    #                 dp[j][j+i] = 1
    #             else:
    #                 for k in range(1, i):
    #                     dp[j][j+i] = min(dp[j][j+i], dp[j][j+k]+dp[j+k][j+i])
    #
    # return dp[0][n-1]
    # ##############

    # ##############
    # Solution 2
    #
    # n = len(nums)
    # if n == 1 and nums[0] >= 0:
    #     return 0
    #
    # dp = []
    # for i in range(n):
    #     dp.append(-1)
    #
    # layer = 1
    # stack = [0]
    # new_stack = []
    #
    # while True:
    #     if len(stack) == 0:
    #         stack = new_stack
    #         layer += 1
    #         new_stack = []
    #     idx = stack.pop(0)
    #     for i in range(nums[idx]-1, -1, -1):
    #         if idx + i + 1 >= n - 1:
    #             return layer
    #         if dp[idx + i + 1] == -1:
    #             dp[idx + i + 1] = layer
    #             new_stack.append(idx + i + 1)


    # ##############
    # Solution 3

    n = len(nums)
    if n == 1 and nums[0] >= 0:
        return 0

    minstep = [-1] * n
    minstep[0] = 0

    stack = [0]

    while stack:
        idx = stack.pop(0)

        for i in range(idx+nums[idx], idx, -1):
            if i >= n-1:
                return minstep[idx] + 1
            if minstep[i] == -1:
                minstep[i] = minstep[idx] + 1
                stack.append(i)
            else:
                break



if __name__ == '__main__':
    print jump([2,3,1,1,4])

