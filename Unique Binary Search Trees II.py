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


def generateTrees(n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """

    def node(val, leftnode, rightnode):

        root = TreeNode(val)
        root.left = leftnode
        root.right = rightnode

        return root


    def subgenerateTrees(mini, maxi):

        return [node(mid, left, right) for mid in range(mini, maxi+1)
                for left in subgenerateTrees(mini, mid-1)
                for right in subgenerateTrees(mid+1, maxi)] or [None]

    if n == 0:
        return []
    
    return subgenerateTrees(1, n)

if __name__ == '__main__':

    treelist = generateTrees(4)

    print len(treelist)
    for tree in treelist:
        print inorderTraversal(tree)
