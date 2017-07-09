def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """

    res = 0

    parentheses_stack = []
    pairlist = [0]

    for i in range(len(s)):
        if s[i] == '(':
            parentheses_stack.append(s[i])
            pairlist.append(0)
        else:
            if len(parentheses_stack) != 0 and parentheses_stack[-1] == '(':
                parentheses_stack.pop(-1)

                p = pairlist.pop(-1) + 1
                if len(pairlist) != 0:
                    pairlist[-1] += p
                else:
                    pairlist.append(p)
            else:
                if len(pairlist) != 0:
                    print pairlist
                    if len(parentheses_stack) == 0:
                        res = max(res, sum([2 * p for p in pairlist]))
                    else:
                        res = max(res, max([2 * p for p in pairlist]))
                parentheses_stack = []
                pairlist = []

    print pairlist
    print parentheses_stack
    if len(pairlist) != 0:
        if len(parentheses_stack) == 0:
            res = max(res, sum([2 * p for p in pairlist]))
        else:
            res = max(res, max([2 * p for p in pairlist]))
    return res



if __name__ == '__main__':
    print longestValidParentheses('())(())(')