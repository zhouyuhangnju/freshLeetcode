# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxPathSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def subMaxPathSum(currroot):

        if not currroot:
            return -2**31, -2**31

        leftlen, leftmax = subMaxPathSum(currroot.left)
        rightlen, rightmax = subMaxPathSum(currroot.right)

        currmax = max(max(0, leftlen) + max(0, rightlen) + currroot.val, leftmax, rightmax)
        currlen = max(max(0, leftlen), max(0, rightlen)) + currroot.val

        return currlen, currmax

    return subMaxPathSum(root)[1]


if __name__ == '__main__':

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)

    print maxPathSum(root)
