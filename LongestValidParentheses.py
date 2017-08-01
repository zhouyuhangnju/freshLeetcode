def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """

def longestValidParentheses(s):

    maxlen = 0
    stack = []
    totalstart = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(['(', i])
        else:
            if len(stack) > 0:
                start = stack.pop(-1)[1]
                maxlen = max(maxlen, i - start + 1)
                if len(stack) > 0:
                    maxlen = max(maxlen, i - stack[-1][1])
                else:
                    maxlen = max(maxlen, i - totalstart + 1)
            else:
                totalstart = i + 1
        print maxlen

    return maxlen



if __name__ == '__main__':
    print longestValidParentheses('(()))())')