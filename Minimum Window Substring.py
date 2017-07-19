import collections

def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    need = collections.Counter(t)
    reslen = len(t)

    i = 0
    I, J = 0, 0
    for j, c in enumerate(s):
        reslen -= need[c] > 0
        need[c] -= 1
        if reslen == 0:
            print need
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            # print i, j, I, J
            if J == 0 or j - i < J - I:
                I, J = i, j + 1
                print I, J

    if reslen == 0:
        return s[I:J]
    else:
        return ''


if __name__ == '__main__':
    print minWindow("ab", "a")