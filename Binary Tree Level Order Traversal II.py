# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrderBottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    if not root:
        return []

    queue = [[root, 0]]
    res = []

    while queue:
        node = queue.pop(0)

        if node[1] >= len(res):
            res.append([node[0].val])
        else:
            res[node[1]].append(node[0].val)

        if node[0].left:
            queue.append([node[0].left, node[1]+1])
        if node[0].right:
            queue.append([node[0].right, node[1]+1])

    return res[::-1]


if __name__ == '__main__':
    root = TreeNode(1)
    # root.left = TreeNode(2)
    root.right = TreeNode(2)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    # root = None

    print levelOrderBottom(root)