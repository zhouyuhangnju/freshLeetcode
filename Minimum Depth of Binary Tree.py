# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def minDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """

    if not root:
        return 0

    stack = [[root, 1]]

    while stack:
        node = stack.pop(0)

        if not node[0].left and not node[0].right:
            return node[1]

        if node[0].left:
            stack.append([node[0].left, node[1]+1])

        if node[0].right:
            stack.append([node[0].right, node[1] + 1])


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)

    # root = None

    print minDepth(root)