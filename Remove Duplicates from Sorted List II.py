# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    if not head:
        return head

    prehead = ListNode(head.val - 1)
    prehead.next = head

    p = prehead
    while p.next:
        checkp = p.next
        flag = 0
        while checkp.next and checkp.next.val == checkp.val:
            checkp = checkp.next
            flag = 1
        if flag == 1:
            p.next = checkp.next
        else:
            p = p.next

    return prehead.next


if __name__ == '__main__':
    vallist = [1,1]

    head, p = None, None
    for i in range(len(vallist)):
        if i == 0:
            head = ListNode(vallist[i])
            p = head
        else:
            node = ListNode(vallist[i])
            p.next = node
            p = p.next

    head = deleteDuplicates(head)

    p = head
    while p:
        print p.val,
        p = p.next