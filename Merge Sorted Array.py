def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """

    for i in range(m+n-1, n-1, -1):
        nums1[i] = nums1[i-n]

    i, j = n, 0
    currpos = 0

    while i < m + n or j < n:
        if i == m + n:
            nums1[currpos] = nums2[j]
            currpos += 1
            j += 1
        elif j == n:
            nums1[currpos] = nums1[i]
            currpos += 1
            i += 1
        else:
            if nums1[i] <= nums2[j]:
                nums1[currpos] = nums1[i]
                currpos += 1
                i += 1
            else:
                nums1[currpos] = nums2[j]
                currpos += 1
                j += 1


if __name__ == '__main__':
    nums1 = [1,3,5,7,9,0,0,0,0,0,0,0]
    nums2 = [2,4]
    merge(nums1, 5, nums2, 2)
    print nums1