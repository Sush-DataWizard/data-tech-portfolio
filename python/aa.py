def parse_positions(pos_list):
    """Convert list like ['apple 100'] into dict {'apple': 100}"""
    pos = {}
    for item in pos_list:
        name, qty = item.split()[:2]
        pos[name] = int(qty)
    return pos

def apply_transactions(start_pos, txn_list):
    """Apply transactions to starting positions"""
    pos = start_pos.copy()
    for txn in txn_list:
        name, qty, ttype, _ = txn.split()
        qty = int(qty)

        if ttype == "SL":   # Sell → reduce position
            pos[name] = pos.get(name, 0) - qty
        elif ttype == "BY": # Buy → increase position
            pos[name] = pos.get(name, 0) + qty
    return pos

def reconcile(pos0, txn1, pos1):
    start = parse_positions(pos0)
    expected = apply_transactions(start, txn1)
    actual = parse_positions(pos1)

    print("Start:   ", start)
    print("Expected:", expected)
    print("Actual:  ", actual)

    # Compare
    diffs = {}
    all_keys = set(expected) | set(actual)
    print("All keys:", all_keys)
    for k in all_keys:
        if expected.get(k, 0) != actual.get(k, 0):
            diffs[k] = (expected.get(k, 0), actual.get(k, 0))
    return diffs


# Example Data
pos0 = ["apple 100", "google 200", "cash 10"]
txn1 = ["apple 50 SL 30000", "google 10 BY 10000"]
pos1 = ["google 20", "cash 100"]

diffs = reconcile(pos0, txn1, pos1)
print("\nDifferences:", diffs)
