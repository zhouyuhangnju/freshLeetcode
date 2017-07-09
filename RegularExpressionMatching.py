
def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    # print s, p
    
    n1, n2 = len(s), len(p)

    if n1 == 0 and n2 == 0:
        return True
    elif n1 > 0 and n2 == 0:
        return False
    else:
        if n2 > 1 and p[1] == '*':
            pchar = p[0]
            i = 0
            flag = False
            while i < n1:
                if pchar == '.' or s[i] == pchar:
                    flag = isMatch(s[i:], p[2:])
                    if flag:
                        break
                    i += 1
                else:
                    break
            if i == 0:
                return isMatch(s[i:], p[2:])
            else:
                return flag or isMatch(s[i:], p[2:])
        else:
            if n1 == 0:
                return False
            else:
                if p[0] == '.' or s[0] == p[0]:
                    return isMatch(s[1:], p[1:])
                else:
                    return False


if __name__ == '__main__':
    print isMatch("bbbba", ".*a*a")