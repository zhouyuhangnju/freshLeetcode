# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseKGroup(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
        """

    prehead = ListNode(None)
    prehead.next = head

    pre = prehead

    while pre is not None:
        p = pre.next

        i = 0
        while p is not None and i < k - 1:
            q = p.next
            if q is None:
                break
            else:
                p.next = q.next
                q.next = pre.next
                pre.next = q
                i += 1

        if i == k - 1:
            pre = p
        else:
            p = pre.next
            j = 0
            while j < i:
                q = p.next
                p.next = q.next
                q.next = pre.next
                pre.next = q
                j += 1
            break

    return prehead.next


if __name__ == '__main__':

    lists = [ListNode(i) for i in range(8)]

    for i in range(len(lists)):
        if i != len(lists) - 1:
            lists[i].next = lists[i + 1]

    res = reverseKGroup(lists[0], 3)

    while res is not None:
        print res.val,
        res = res.next