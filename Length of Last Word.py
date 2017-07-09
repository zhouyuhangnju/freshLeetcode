def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """

    words = s.split(' ')

    res = 0
    for i in range(len(words)-1, -1, -1):
        if len(words[i]) > 0:
            res = len(words[i])
            break

    return res



if __name__ == '__main__':
    print lengthOfLastWord('aaaa    ')