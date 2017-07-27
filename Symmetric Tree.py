# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    if not root:
        return True

    inorderlist = []
    nodestack = [[root, 0, -1]]

    while(nodestack):
        node = nodestack.pop(-1)

        if node[1] == 0:
            node[1] = 1
            nodestack.append(node)

            if node[0].left:
                nodestack.append([node[0].left, 0, 0])

        elif node[1] == 1:
            inorderlist.append([node[0].val, node[2]])

            if node[0].right:
                nodestack.append([node[0].right, 0, 1])

    print inorderlist

    nodenum = len(inorderlist)
    l = nodenum
    if nodenum % 2 == 1:
        l -= 1

    for i in range(l / 2):
        j = len(inorderlist) - i - 1
        if inorderlist[i][0] != inorderlist[j][0] or inorderlist[i][1] + inorderlist[j][1] != 1:
            return False

    return True


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    # root = None

    print isSymmetric(root)