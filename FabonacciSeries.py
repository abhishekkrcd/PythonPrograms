#This Python Code generates the Fibonacci series up to a specified number of terms.
def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

if __name__ == "__main__":
    terms = int(input("Enter the number of terms for Fibonacci series: "))
    print(f"Fibonacci series up to {terms} terms: {fibonacci_series(terms)}")