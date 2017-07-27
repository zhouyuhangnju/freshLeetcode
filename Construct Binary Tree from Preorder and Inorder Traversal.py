# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """

    if len(preorder) == 0:
        return None

    root = TreeNode(preorder[0])

    idx = inorder.index(preorder[0])

    root.left = buildTree(preorder[1:idx+1], inorder[:idx])
    root.right = buildTree(preorder[idx+1:], inorder[idx+1:])

    return root



if __name__ == '__main__':
    tree = buildTree([1,2,4,5,3,7], [4,2,5,1,3,7])

    print tree.val
    print tree.left.val
    print tree.right.val
    print tree.left.left.val
    print tree.left.right.val
    # print tree.right.left.val
    print tree.right.right.val
