# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


# @param root, a tree link node
# @return nothing
def connect(root):

    if not root:
        return

    rightdict = {}

    def subConnect(currroot, layer):

        if currroot.left:
            subConnect(currroot.left, layer + 1)

        if currroot.right:
            subConnect(currroot.right, layer + 1)

        if layer in rightdict:
            preright = rightdict[layer]
            preright.next = currroot

        rightdict[layer] = currroot

    subConnect(root, 0)

if __name__ == '__main__':
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    root.left.left = TreeLinkNode(4)
    root.left.right = TreeLinkNode(5)
    # root.right.left = TreeLinkNode(6)
    root.right.right = TreeLinkNode(7)

    connect(root)

    print root.next
    print root.left.next.val
    print root.right.next
    print root.left.left.next.val
    print root.left.right.next.val
    # print root.right.left.next.val
    print root.right.right.next
