# Definition for singly-linked list.
from Queue import PriorityQueue

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    head = ListNode(None)
    currnode = head
    q = PriorityQueue()

    for node in lists:
        if node is not None:
            q.put((node.val, node))

    while q.qsize() > 0:
        currnode.next = q.get()[1]
        currnode = currnode.next

        if currnode.next is not None:
            q.put((currnode.next.val, currnode.next))

    return head.next


if __name__ == '__main__':
    print mergeKLists([ListNode(3), ListNode(2)]).val