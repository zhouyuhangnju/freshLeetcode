def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    res = []

    candidates = sorted(candidates)

    def combinationRemain(remain, curr_res):

        if remain == 0:
            res.append(curr_res)
            return

        for c in candidates:
            if c > remain:
                break
            if curr_res and c < curr_res[-1]:
                continue
            combinationRemain(remain - c, curr_res + [c])

    combinationRemain(target, [])

    return res


def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    res = []

    candidates = sorted(candidates)

    def combinationRemain(remain, curr_res, curr_idx):

        if remain == 0:
            res.append(curr_res)
            return

        if remain < 0 or curr_idx >= len(candidates):
            return

        combinationRemain(remain-candidates[curr_idx], curr_res+[candidates[curr_idx]], curr_idx)
        combinationRemain(remain, curr_res, curr_idx + 1)

    combinationRemain(target, [], 0)

    return res


if __name__ == '__main__':
    print combinationSum2([2, 3, 6, 7], 7)