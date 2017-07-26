# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    def subIsValidBST(root, mini, maxi):

        if not root:
            return True

        if root.val < mini or root.val > maxi:
            return False

        return subIsValidBST(root.left, mini, root.val-1) and subIsValidBST(root.right, root.val+1, maxi)

    return subIsValidBST(root, -2**31, 2**31-1)


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)

    print isValidBST(root)