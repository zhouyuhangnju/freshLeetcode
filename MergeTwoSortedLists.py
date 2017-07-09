# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    p1, p2 = l1, l2

    resl = None
    while p1 is not None and p2 is not None:
        print p1.val, p2.val
        if p1.val < p2.val:
            nextp = p1
            p1 = p1.next
        else:
            nextp = p2
            p2 = p2.next

        if resl is None:
            resl = nextp
            resp = resl
        else:
            resp.next = nextp
            resp = nextp

    if p1 is None:
        if resl is None:
            resl = p2
        else:
            resp.next = p2
    elif p2 is None:
        if resl is None:
            resl = p1
        else:
            resp.next = p1

    return resl


if __name__ == '__main__':
    print mergeTwoLists(None, None)