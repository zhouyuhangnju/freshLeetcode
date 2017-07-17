def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """

    a = list(a)[::-1]
    b = list(b)[::-1]
    print a, b

    carry = '0'

    if len(a) > len(b):
        a, b = b, a

    minlen = len(a)

    res = [bb for bb in b]
    for i in range(minlen):
        if a[i] == '0' and b[i] == '0' and carry == '1':
            res[i] = '1'
            carry = '0'
        elif a[i] == '0' and b[i] == '1' and carry == '1':
            res[i] = '0'
        elif a[i] == '1' and b[i] == '0' and carry == '0':
            res[i] = '1'
        elif a[i] == '1' and b[i] == '1' and carry == '0':
            res[i] = '0'
            carry = '1'
    if carry == '1':
        for i in range(minlen, len(b)):
            if b[i] == '0' and carry == '1':
                res[i] = '1'
                carry = '0'
                break
            elif b[i] == '1' and carry == '1':
                res[i] = '0'

    if carry == '1':
        res.append('1')

    res = ''.join(res[::-1])

    return res


if __name__ == '__main__':
    print addBinary('11', '1')