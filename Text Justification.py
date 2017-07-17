def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """

    res = []

    currstr = ''
    currnum = 0
    for i in range(len(words)):
        if len(currstr) == 0:
            if len(words[i]) <= maxWidth:
                currstr += words[i]
                currnum += 1
            else:
                return []
        else:
            if len(currstr) + 1 + len(words[i]) <= maxWidth:
                currstr += ' '
                currstr += words[i]
                currnum += 1
            else:
                print currstr
                if len(currstr) != maxWidth:
                    spacenum = maxWidth - len(currstr) + currnum - 1
                    print spacenum
                    if currnum == 1:
                        spacenum = maxWidth - len(currstr)
                        currstr += ' ' * spacenum
                    else:
                        a, b = divmod(spacenum, currnum-1)
                        print a, b
                        strs = currstr.split()
                        currstr = ''
                        for j in range(len(strs)):
                            currstr += strs[j]
                            if j != len(strs) - 1:
                                currstr += ' ' * a
                                if b > 0:
                                    currstr += ' '
                                    b -= 1
                res.append(currstr)
                currstr = words[i]
                currnum = 1

    spacenum = maxWidth - len(currstr)
    currstr += ' ' * spacenum
    res.append(currstr)

    return res

if __name__ == '__main__':
    print fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)