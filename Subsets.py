def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    n = len(nums)

    def pickksubset(n, k):

        kres = []

        def subpickksubset(start, curr):
            if len(curr) == k:
                kres.append(curr)
            else:
                for i in range(start, n):
                    subpickksubset(i+1, curr + [i])

        if k <= n / 2:
            subpickksubset(0, [])
        else:
            k = n - k
            subpickksubset(0, [])
            kres = [list(set(range(n)) - set(r)) for r in kres]

        return kres

    res = []

    for i in range(0, n + 1):
        res += pickksubset(n, i)

    resnums = []
    for r in res:
        resnums.append([nums[i] for i in r])

    return resnums




if __name__ == '__main__':
    print subsets([1,2,4,5])