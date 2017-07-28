# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def flatten(root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """

    res = []

    def postTravel(currroot):

        res.append(currroot)

        if currroot.left:
            postTravel(currroot.left)

        if currroot.right:
            postTravel(currroot.right)

    if not root:
        return

    postTravel(root)
    for i in range(len(res)-1):
        res[i].left = None
        res[i].right = res[i+1]


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

    root = None

    flatten(root)

    p = root
    while p:
        print p.val
        p = p.right