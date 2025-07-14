def merge(intervals):
    if not intervals:
        return []

    # Step 1: Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    print(intervals)

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:  # Overlapping
            last[1] = max(last[1], current[1])  # Merge
        else:
            merged.append(current)  # No overlap

    return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))