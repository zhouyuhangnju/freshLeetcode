# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(inorder, postorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """

    if len(postorder) == 0:
        return None

    root = TreeNode(postorder[-1])

    idx = inorder.index(postorder[-1])

    root.left = buildTree(inorder[:idx], postorder[:idx])
    root.right = buildTree(inorder[idx+1:], postorder[idx:-1])

    return root



if __name__ == '__main__':
    tree = buildTree([4,2,5,1,6,3,7], [4,5,2,6,7,3,1])

    print tree.val
    print tree.left.val
    print tree.right.val
    print tree.left.left.val
    print tree.left.right.val
    print tree.right.left.val
    print tree.right.right.val
