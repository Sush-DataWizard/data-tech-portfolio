# Generate Fibonacci series up to n terms

def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Example usage
n = 10
print(f"Fibonacci series up to {n} terms: {fibonacci_series(n)}")