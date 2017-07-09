def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    def NSum(N, nums, target):

        if N < 2 or N > len(nums) or N * nums[0] > target or N * nums[-1] < target:
            return []

        reslist = []

        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    reslist.append([nums[l], nums[r]])

                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    while l < r and nums[r-1] == nums[r]:
                        r -= 1

                    l += 1
                    r -= 1
        else:
            i = len(nums) - 1
            while i > 0:
                print nums[i]
                subreslist = NSum(N-1, nums[0:i], target-nums[i])

                for res in subreslist:
                    print res
                    res.append(nums[i])
                    reslist.append(res)

                while i > 0 and nums[i-1] == nums[i]:
                    i -= 1
                i -= 1

        return reslist

    nums = sorted(nums)
    reslist = NSum(4, nums, target)
    return reslist


if __name__ == '__main__':
    print fourSum([1, 0, -1, 0, -2, 2], 0)