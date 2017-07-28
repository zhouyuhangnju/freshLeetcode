# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedListToBST(head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """

    def subSortedListToBST(currhead, currlen):

        if currlen <= 0:
            return None

        mid = currlen / 2

        p = currhead
        count = 0
        while count < mid:
            p = p.next
            count += 1

        root = TreeNode(p.val)
        root.left = subSortedListToBST(currhead, mid)
        root.right = subSortedListToBST(p.next, currlen-mid-1)

        return root


    l = 0
    p = head
    while p:
        l += 1
        p = p.next

    print l

    return subSortedListToBST(head, l)


if __name__ == '__main__':
    vallist = [1, 2, 3, 4, 5, 6, 7]

    head, p = None, None
    for i in range(len(vallist)):
        if i == 0:
            head = ListNode(vallist[i])
            p = head
        else:
            node = ListNode(vallist[i])
            p.next = node
            p = p.next

    root = sortedListToBST(head)

    print root.val
    print root.left.val
    print root.right.val

    print root.left.left.val
    print root.left.right.val

    print root.right.left.val
    print root.right.right.val