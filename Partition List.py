# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def partition(head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """

    prehead = ListNode(x-1)
    prehead.next = head

    curr = prehead
    pre = prehead
    p = head
    while p:
        if p.val < x:
            if p == curr.next:
                pre = p
            else:
                pre.next = p.next
                p.next = curr.next
                curr.next = p
            curr = p
            p = pre.next
        else:
            pre = p
            p = p.next

    return prehead.next


if __name__ == '__main__':
    vallist = [1, 4, 3, 2, 5, 2]

    head, p = None, None
    for i in range(len(vallist)):
        if i == 0:
            head = ListNode(vallist[i])
            p = head
        else:
            node = ListNode(vallist[i])
            p.next = node
            p = p.next

    head = partition(head, 3)

    p = head
    while p:
        print p.val,
        p = p.next
