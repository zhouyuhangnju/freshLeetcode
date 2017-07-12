def sort_printer_queue(queue):

    def sub_sort(idx, queue):

        if len(queue) <= 0:
            return []

        i, j = 0, len(queue) - 1

        orientation = -1
        p = i
        while i < j:
            if orientation == -1:
                if queue[j] > queue[p]:
                    queue[j], queue[p] = queue[p], queue[j]
                    idx[j], idx[p] = idx[p], idx[j]
                    p = j
                    i += 1
                    orientation = 1
                else:
                    j -= 1
            elif orientation == 1:
                if queue[i] < queue[p]:
                    queue[i], queue[p] = queue[p], queue[i]
                    idx[i], idx[p] = idx[p], idx[i]
                    p = i
                    j -= 1
                    orientation = -1
                else:
                    i += 1

        left_sorted = sub_sort(idx[0:p], queue[0:p])
        right_sorted = sub_sort(idx[p+1:], queue[p+1:])

        return left_sorted + [idx[p]] + right_sorted

    sorted_idx = sub_sort(range(len(queue)), [i for i in queue])

    for i in range(1, len(sorted_idx)):
        if queue[sorted_idx[i]] == queue[sorted_idx[i-1]] and sorted_idx[i] < sorted_idx[i-1]:
            sorted_idx[i-1], sorted_idx[i] = sorted_idx[i], sorted_idx[i-1]

    return sorted_idx


if __name__ == '__main__':
    print sort_printer_queue([6])