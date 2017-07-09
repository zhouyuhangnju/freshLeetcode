def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    def subpermute(nums):
        res = []
        if len(nums) == 0:
            res.append([])
        else:
            for i, n in enumerate(nums):
                if i > 0 and n == nums[i-1]:
                    continue
                subres = subpermute(nums[:i] + nums[i+1:])
                for p in subres:
                    res.append([n] + p)
        return res

    nums = sorted(nums)
    res = subpermute(nums)

    return res

    # return [[n] + p for i, n in enumerate(nums) for p in permute(nums[:i] + nums[i+1:])] if len(nums) != 0 else [[]]

if __name__ == '__main__':
    print permute([1,1,3,3])