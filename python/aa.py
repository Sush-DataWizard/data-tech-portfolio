def similar_pairs(A, B):
    from collections import defaultdict
    MOD = 10**9 + 7
    
    freq = defaultdict(int)
    ans = 0
    print(freq)

    for j in range(len(A)):

        ans = (ans + freq[A[j]]) % MOD
        freq[A[j]] += 1
        
        if j - B >= 0:
            freq[A[j-B]] -= 1
            if freq[A[j-B]] == 0:
                del freq[A[j-B]]
    
    return ans % MOD


print(similar_pairs([1, 2, 1, 3, 1, 4], 2))  # Output: 2
# print(similar_pairs([12, 11, 8, 1], 14))     # Output: 0
