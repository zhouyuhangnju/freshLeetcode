def plusOne(digitslist):
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    digitslist = digitslist[::-1]

    carry = 1
    for i in range(len(digitslist)):
        digitslist[i] += 1
        if digitslist[i] < 10:
            carry = 0
            break
        else:
            digitslist[i] = 0

    if carry == 1:
        digitslist.append(1)

    digitslist = digitslist[::-1]

    return digitslist



if __name__ == '__main__':
    print plusOne([9])