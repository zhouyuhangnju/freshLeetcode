# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def insert(intervals, newInterval):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
        """

    inserted_intervals = []

    if len(intervals) == 0:
        inserted_intervals.append(newInterval)
    else:
        idx = 0
        while idx < len(intervals) and newInterval.start > intervals[idx].start:
            inserted_intervals.append(intervals[idx])
            idx += 1

        if len(inserted_intervals) > 0 and newInterval.start <= inserted_intervals[-1].end:
            inserted_intervals[-1].end = max(newInterval.end, inserted_intervals[-1].end)
        else:
            inserted_intervals.append(newInterval)

        while idx < len(intervals) and intervals[idx].start <= inserted_intervals[-1].end:
            inserted_intervals[-1].end = max(intervals[idx].end, inserted_intervals[-1].end)
            idx += 1

        for i in range(idx, len(intervals)):
            inserted_intervals.append(intervals[i])

    return inserted_intervals


if __name__ == '__main__':
    intervals = [Interval(1, 5)]
    inserted_intervals = insert(intervals, Interval(2, 3))

    for interval in inserted_intervals:
        print interval.start, interval.end