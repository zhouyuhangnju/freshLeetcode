# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """

    if p == None and q == None:
        return True

    elif p == None or q == None:
        return False

    else:
        if p.val != q.val:
            return False
        else:
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)



if __name__ == '__main__':
    p = TreeNode(1)
    q = TreeNode(1)
    p.right = TreeNode(2)
    q.right = TreeNode(2)

    print isSameTree(p, q)