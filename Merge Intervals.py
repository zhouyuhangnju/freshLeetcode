# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """

    intervals = sorted(intervals, key=lambda i: i.start)

    merged_intervals = []
    for interval in intervals:
        if len(merged_intervals) > 0 and interval.start <= merged_intervals[-1].end:
            merged_intervals[-1].end = max(interval.end, merged_intervals[-1].end)
        else:
            merged_intervals.append(interval)

    return merged_intervals


if __name__ == '__main__':
    intervals = [Interval(1, 3), Interval(8, 10), Interval(2, 6), Interval(15, 18)]
    merged_intervals = merge(intervals)

    for interval in merged_intervals:
        print interval.start, interval.end
