def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    def subSubsetsWithDup(currnums, reslist):
        if len(currnums) == 0:
            return [res[0] for res in reslist]

        newreslist = []
        for i in range(len(reslist)):
            if currnums[0] not in reslist[i][1]:
                newreslist.append([reslist[i][0] + [currnums[0]], []])
                reslist[i][1] += [currnums[0]]
        reslist += newreslist

        return subSubsetsWithDup(currnums[1:], reslist)

    nums = sorted(nums)
    return subSubsetsWithDup(nums, [[[], []]])



if __name__ == '__main__':
    print subsetsWithDup([1,2,2,3])