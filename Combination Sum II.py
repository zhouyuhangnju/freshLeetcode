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


def combinationSum22(candidates, target):
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

        if remain < 0 or curr_idx >= len(candidates):
            return

        combinationRemain2(remain - candidates[curr_idx], curr_res + [candidates[curr_idx]], curr_idx + 1)
        j = curr_idx
        while j < len(candidates) and candidates[j] == candidates[curr_idx]:
            j += 1
        combinationRemain2(remain, curr_res, j)

    combinationRemain2(target, [], 0)

    return res



if __name__ == '__main__':
    print combinationSum22([1], 1)