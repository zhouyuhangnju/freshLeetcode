def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    res = []

    candidates = sorted(candidates)

    def combinationRemain2(remain, curr_res, curr_idx):

        if remain == 0:
            res.append(curr_res)
            return

        c = -1
        for i in range(curr_idx, len(candidates)):
            if c == candidates[i]:
                continue
            c = candidates[i]
            if c > remain:
                break
            combinationRemain2(remain - c, curr_res + [c], i + 1)


    combinationRemain2(target, [], 0)

    return res




if __name__ == '__main__':
    print combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)