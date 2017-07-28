# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def hasPathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """

    res = []

    def pathSum(currroot, currpath):

        if not currroot.left and not currroot.right:
            s = currroot.val
            for p in currpath:
                s += p
            if s == sum:
                res.append(currpath + [currroot.val])
        else:
            if currroot.left:
                pathSum(currroot.left, currpath + [currroot.val])

            if currroot.right:
                pathSum(currroot.right, currpath + [currroot.val])

    if not root:
        return []

    pathSum(root, [])
    return res



if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    # root.left.right = TreeNode(5)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    # root = None

    print hasPathSum(root, 22)
