def restoreIpAddresses(s):
    """
    :type s: str
    :rtype: List[str]
    """

    res = []

    def subRestoreIpAddresses(remainS, currstr, layer):

        if len(remainS) == 0:
            if layer == 4:
                res.append(currstr)
            return

        if layer < 4:

            if remainS[0] == '0':
                subRestoreIpAddresses(remainS[1:], currstr + '.0', layer + 1)
            else:
                for i in range(1, 4):
                    if i > len(remainS):
                        break
                    currint = int(remainS[:i])
                    if currint < 256:
                        subRestoreIpAddresses(remainS[i:], currstr + '.{}'.format(currint), layer + 1)

    subRestoreIpAddresses(s, '', 0)

    return [r[1:] for r in res]


if __name__ == '__main__':
    print restoreIpAddresses("11111111111111111")