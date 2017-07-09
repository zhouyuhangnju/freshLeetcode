def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """

    def makenext(needle):
        # print needle
        nextlist = [0]
        for i in range(1, len(needle)):
            j = i - 1
            while j > 0:
                if needle[i-1] == needle[nextlist[j]]:
                    nextlist.append(nextlist[j]+1)
                    break
                else:
                    j = nextlist[j]
            if j == 0:
                nextlist.append(0)
        #     print nextlist
        # print nextlist

        finalnextlist = [0]
        for i in range(1, len(nextlist)):
            if needle[i] != needle[nextlist[i]]:
                finalnextlist.append(nextlist[i])
            else:
                finalnextlist.append(finalnextlist[nextlist[i]])

        return finalnextlist

    if len(haystack) == 0 or len(needle) == 0:
        return -1

    nextlist = makenext(needle)

    i, j = 0, 0
    while i < len(haystack):
        print haystack[i]
        print haystack[i], needle[j]
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == len(needle):
                return i - j
        else:
            print j, nextlist[j]
            if j == 0:
                i += 1
            j = nextlist[j]

    return -1


if __name__ == '__main__':
    print strStr("babcbabcabcaabcabcabcacabc", "abcabcacab")