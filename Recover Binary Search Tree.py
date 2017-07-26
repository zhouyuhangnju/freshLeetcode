# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def recoverTree(root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """

    nodelist = []

    stack = [[root, 0]]

    while stack:
        currNode = stack.pop(-1)
        if currNode[1] == 0:
            currNode[1] = 1
            stack.append(currNode)
            if currNode[0].left:
                stack.append([currNode[0].left, 0])
        elif currNode[1] == 1:
            nodelist.append(currNode[0])
            if currNode[0].right:
                stack.append([currNode[0].right, 0])

    wrongpair = []
    for i in range(1, len(nodelist)):
        if nodelist[i-1].val > nodelist[i].val:
            wrongpair.append([nodelist[i-1], nodelist[i]])

    print len(wrongpair)

    if len(wrongpair) == 1:
        wrongpair[0][0].val, wrongpair[0][1].val = wrongpair[0][1].val, wrongpair[0][0].val
    elif len(wrongpair) == 2:
        wrongpair[0][0].val, wrongpair[1][1].val = wrongpair[1][1].val, wrongpair[0][0].val



if __name__ == '__main__':

    root = TreeNode(20)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(10)

    # root = TreeNode(0)
    # root.left = TreeNode(1)

    recoverTree(root)
    recoverTree(root)