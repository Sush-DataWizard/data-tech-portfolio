def count_splits(s: str) -> int:
    depth = 0
    groups = 0
    for ch in s:
        if ch == '(':
            if depth == 0:  # start of a new top-level group
                groups += 1
            depth += 1
        else:
            depth -= 1
    return 2 ** groups

# Example
s = "()()(())"
print(count_splits(s))  # Output: 8
