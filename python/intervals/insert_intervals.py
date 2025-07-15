
intervals = [[1,3],[6,9]]
newInterval = [2,5]

def insert(intervals,newInterval):
    merged = []
    i = 0
    n = len(intervals)

    # Step 1: Add all intervals before newInterval (no overlap)
    while i < n and intervals[i][1] < newInterval[0]:
        merged.append(intervals[i])
        i += 1

    # Step 2: Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    merged.append(newInterval)

    # Step 3: Add the rest intervals (after newInterval)
    while i < n:
        merged.append(intervals[i])
        i += 1

    return merged

print(insert(intervals,newInterval))
        