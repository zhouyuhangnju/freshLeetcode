# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    def subIsBalanced(currroot):

        if not currroot:
            return True, 0

        lflag, lheight = subIsBalanced(currroot.left)

        if not lflag:
            return False, -1

        rflag, rheight = subIsBalanced(currroot.right)
        if not rflag:
            return False, -1

        print lheight, rheight
        if abs(lheight-rheight) <= 1:
            return True, max(lheight, rheight) + 1
        else:
            return False, -1

    return subIsBalanced(root)[0]


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    root = None

    print isBalanced(root)