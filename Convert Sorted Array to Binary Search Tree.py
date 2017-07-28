# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """

    if len(nums) <=  0:
        return None

    mid = len(nums) / 2

    root = TreeNode(nums[mid])

    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])

    return root


if __name__ == '__main__':

    root = sortedArrayToBST([1,3,4,5,6,7])

    print root.val
    print root.left.val
    print root.right.val

    print root.left.left.val
    print root.left.right.val

    print root.right.left.val
    # print root.right.right.val