def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """

    res = [0] * (len(num1) + len(num2))

    for i in range(len(num1)-1, -1, -1):
        carry = 0
        for j in range(len(num2)-1, -1, -1):
            print i, j,
            tmpres = int(num1[i]) * int(num2[j]) + carry
            print tmpres
            carry, res[i + j + 1] = divmod(res[i + j + 1] + tmpres, 10)
        res[i] += carry
        print res
    res =  ''.join(map(str, res))

    return '0' if not res.lstrip('0') else res.lstrip('0')


if __name__ == '__main__':
    print multiply("581852037460725882246068583352420736139988952640866685633288423526139", "2723349969536684936041476639043426870967112972397011150925040382981287990380531232")