def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """

    subpath = path.split('/')

    res = []
    for p in subpath:
        if len(p) > 0:
            if p == '.':
                continue
            elif p == '..':
                if len(res) > 0:
                    res.pop(-1)
            else:
                res.append(p)

    res = '/' + '/'.join(res)

    return res



if __name__ == '__main__':
    print simplifyPath("/a/./b/../../c/")