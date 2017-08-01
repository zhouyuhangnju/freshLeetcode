
def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """

    res = []

    def subGenerateParenthesis(p, left, right):
        if left > 0:
            subGenerateParenthesis(p+'(', left-1, right)
        if right > left:
            subGenerateParenthesis(p+')', left, right-1)
        if right == 0:
            res.append(p)

    subGenerateParenthesis('', n, n)

    return res if n > 0 else []

def generateParenthesis2(n):
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

    print generateParenthesis(0)