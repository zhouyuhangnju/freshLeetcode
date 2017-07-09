# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """

    length = 0
    node = head
    while node:
        length += 1
        tail = node
        node = node.next

    if length == 0:
        return None

    k = k % length
    if k == 0:
        return head

    node = head
    for i in range(length - k - 1):
        node = node.next

    rotatedhead = node.next
    node.next = None
    tail.next = head

    return rotatedhead

def constructList(n):

    head = ListNode(-1)

    pre = head
    for i in range(n):
        node = ListNode(i)
        pre.next = node
        pre = node
    pre.next = None

    return head.next

if __name__ == '__main__':

    head = constructList(3)
    rotatedhead = rotateRight(head, 4)


    node = rotatedhead
    while node:
        print node.val,
        node = node.next


