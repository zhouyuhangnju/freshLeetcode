def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    lowercase = 'abcdefghijklmnopqrstuvwxyz0123456789'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    I, J = 0, len(s) - 1

    while I < J:

        idxi = max(lowercase.find(s[I]), uppercase.find(s[I]))
        if idxi == -1:
            I += 1
            continue

        idxj = max(lowercase.find(s[J]), uppercase.find(s[J]))
        if idxj == -1:
            J -= 1
            continue

        if idxi != idxj:
            return False

        I += 1
        J -= 1

    return True



if __name__ == '__main__':
    print isPalindrome("0P")