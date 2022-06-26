def mergeOverlappingIntervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    print(f"Sorted intervals: {intervals}")
    for (idx, item) in enumerate(intervals[:-1]):
        next_item = intervals[idx+1]
        s_num, e_num = item
        n_s_num, n_e_num = next_item

        # two interval has overlap
        if e_num >= n_s_num and e_num < n_e_num:
            print(f"merge {item} + {next_item} => [{s_num}, {n_e_num}]")
            new_item = [s_num, n_e_num]
            # replace the merged interval(first)
            intervals[idx] = new_item
            # remove the merged interval(second)
            del intervals[idx+1]
            return mergeOverlappingIntervals(intervals)

        # next interval is subset of previous interval
        if e_num >= n_s_num and e_num >= n_e_num:
            del intervals[idx+1]
            return mergeOverlappingIntervals(intervals)

    return intervals