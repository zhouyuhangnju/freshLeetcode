def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """

    if endWord not in wordList:
        return 0

    if beginWord in wordList:
        wordList.remove(beginWord)

    currlist = [beginWord]
    currlen = 1

    while currlist:
        currlen += 1
        newlist = []
        for xword in currlist:
            currnewlist = []
            for yword in wordList:
                count = 0
                for xchar, ychar in zip(xword, yword):
                    if xchar != ychar:
                        count += 1
                    if count >= 2:
                        break
                if count < 2:
                    if yword == endWord:
                        return currlen
                    currnewlist.append(yword)
            for yword in currnewlist:
                wordList.remove(yword)
            newlist += currnewlist
        currlist = newlist

    return 0




if __name__ == '__main__':
    print ladderLength("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"])