def fibonacci(n):
    fib_series = [0, 1]
    for _ in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series


num_terms = int(input("Enter the number of terms for the Fibonacci series: "))

fibonacci_series = fibonacci(num_terms)
print("Fibonacci Series:", fibonacci_series)
