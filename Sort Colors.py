def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    def quicksort(nums):

        def subquicksort(nums, start, end):

            if start >= end:
                return
            
            p = nums[start]
            i, j, direction = start, end, -1
            while i < j:
                if direction == -1:
                    if nums[j] < p:
                        nums[i] = nums[j]
                        i += 1
                        direction = 1
                    else:
                        j -= 1
                elif direction == 1:
                    if nums[i] > p:
                        nums[j] = nums[i]
                        j -= 1
                        direction = -1
                    else:
                        i += 1

            assert i == j
            nums[i] = p

            subquicksort(nums, start, i - 1)
            subquicksort(nums, i + 1, end)

        subquicksort(nums, 0, len(nums)-1)

    quicksort(nums)



if __name__ == '__main__':
    colors = [2,1,2,3,1,1]
    sortColors(colors)
    print colors