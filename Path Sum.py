# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def hasPathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """

    def pathSum(currroot):

        currsumlist = []
        if currroot.left:
            currsumlist += pathSum(currroot.left)
        if currroot.right:
            currsumlist += pathSum(currroot.right)

        return [c + currroot.val for c in currsumlist] if currsumlist else [currroot.val]

    return sum in pathSum(root) if root else False



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)

    # root = None
    # 
    print hasPathSum(root, 8)
