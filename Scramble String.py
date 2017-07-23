def isScramble(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """

    def subIsScramble(s1, s2, dpdict):
        assert len(s1) == len(s2)

        if len(s1) == 0:
            # print s1, s2, True
            return True

        if s1 == s2:
            # print s1, s2, True
            return True

        key = s1 + s2
        if key in dpdict:
            # print s1, s2, dpdict[key]
            return dpdict[key]

        if set(s1) != set(s2):
            return False

        res = False
        for i in range(1, len(s1)):
            res1 = subIsScramble(s1[:i], s2[:i], dpdict) and subIsScramble(s1[i:], s2[i:], dpdict)
            res2 = subIsScramble(s1[:i], s2[-i:], dpdict) and subIsScramble(s1[i:], s2[:-i], dpdict)
            res = res or res1 or res2

        dpdict[key] = res
        # print s1, s2, res
        return res


    return subIsScramble(s1, s2, {})


if __name__ == '__main__':
    print isScramble("qircluqkyzmiqlhnzxrnbgqoqshpyr", "xmuhqrpqcgynlnlbzhiyrqiqoqskzr")