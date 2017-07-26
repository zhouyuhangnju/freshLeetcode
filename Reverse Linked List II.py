# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseBetween(head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """

    prehead = ListNode(None)
    prehead.next = head

    p = prehead
    for i in range(m - 1):
        p = p.next

    print p.val

    q = p.next
    for i in range(n - m):
        qnext = q.next
        q.next = qnext.next
        qnext.next = p.next
        p.next = qnext

    return prehead.next


if __name__ == '__main__':
    vallist = [1,2,3,4,5]

    head, p = None, None
    for i in range(len(vallist)):
        if i == 0:
            head = ListNode(vallist[i])
            p = head
        else:
            node = ListNode(vallist[i])
            p.next = node
            p = p.next

    reversedhead = reverseBetween(head, 2, 4)

    p = reversedhead
    while p:
        print p.val,
        p = p.next