
def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """

    reslist = [('(', 1)]
    for i in range(n * 2 - 1):
        newreslist = []
        for res in reslist:
            if res[1] > 0:
                if n * 2 - len(res[0]) <= res[1]:
                    newreslist.append((res[0] + ')', res[1] - 1))
                else:
                    newreslist.append((res[0] + '(', res[1] + 1))
                    newreslist.append((res[0] + ')', res[1] - 1))
            else:
                newreslist.append((res[0] + '(', res[1] + 1))
        reslist = newreslist

    return [res[0] for res in reslist]


if __name__ == '__main__':
    print generateParenthesis(4)