def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    if len(strs) == 0:
        return ''

    commprefix = ''

    flag = True
    i = 0
    while flag:
        if len(strs[0]) <= i:
            flag = False
        else:
            currchar = strs[0][i]
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[j][i] != currchar:
                    flag = False
            if flag:
                commprefix += currchar
                i += 1

    return commprefix


if __name__ == '__main__':
    print longestCommonPrefix(["abc", 'abcd', 'abef'])