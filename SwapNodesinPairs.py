# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    prehead = ListNode(None)
    prehead.next = head

    pre = prehead

    while pre.next is not None and pre.next.next is not None:
        p = pre.next
        q = p.next

        p.next = q.next
        pre.next = q
        q.next = p

        pre = p

    return prehead.next

if __name__ == '__main__':
    lists = [ListNode(i) for i in range(6)]

    for i in range(len(lists)):
        if i != len(lists) - 1:
            lists[i].next = lists[i + 1]

    res = swapPairs(lists[0])

    while res is not None:
        print res.val,
        res = res.next
