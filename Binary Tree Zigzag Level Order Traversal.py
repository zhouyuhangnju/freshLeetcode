# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    if not root:
        return []

    queue = [[root, 0]]
    res = []

    currres = []
    currlevel = 0
    while queue:
        # print len(queue)
        node = queue.pop(0)
        print node[0].val, node[1]

        # print node[1], currlevel
        if node[1] == currlevel:
            currres.append(node[0].val)
        else:
            # print node[1]
            if currlevel % 2 == 0:
                res.append(currres)
            elif currlevel % 2 == 1:
                res.append(currres[::-1])
            currres = [node[0].val]
            currlevel = node[1]

        if node[0].left:
            queue.append([node[0].left, node[1] + 1])
        if node[0].right:
            queue.append([node[0].right, node[1] + 1])

    if currlevel % 2 == 0:
        res.append(currres)
    elif currlevel % 2 == 1:
        res.append(currres[::-1])

    return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # root = None

    print zigzagLevelOrder(root)