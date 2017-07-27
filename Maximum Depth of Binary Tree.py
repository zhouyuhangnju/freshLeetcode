# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def subMaxDepth(r, level):
        return max(level, subMaxDepth(r.left, level+1), subMaxDepth(r.right, level+1)) if r else level-1

    return subMaxDepth(root, 1)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)

    print maxDepth(root)