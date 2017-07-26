# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    res = []

    rootstack = []
    rootstack.append([root, 0])

    while rootstack:
        [currroot, time] = rootstack.pop(-1)
        if currroot != None:
            if time == 0:
                rootstack.append([currroot, 1])
                rootstack.append([currroot.left, 0])
            elif time == 1:
                res.append(currroot.val)
                rootstack.append([currroot.right, 0])

    return res

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print inorderTraversal(root)