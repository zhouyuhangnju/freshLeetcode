from itertools import groupby

def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """

    if n == 0:
        return ''

    s = '1'

    for _ in range(n-1):
        s = ''.join(str(len(list(group))) + digit for digit, group in groupby(s))
    return s


if __name__ == '__main__':
    print countAndSay(10)