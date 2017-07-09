def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    validdict = {'(':')', '[':']', '{':'}'}

    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stack.append(s[i])
        else:
            if len(stack) <= 0:
                return False
            top = stack.pop(-1)
            if s[i] != validdict[top]:
                return False

    if len(stack) > 0:
        return False

    return True


if __name__ == '__main__':
    print isValid("())")