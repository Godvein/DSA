def fib(n):
    # Base cases
    if n == 0:
        return 0  # O(1)
    elif n == 1:
        return 1  # O(1)
    else:
        # Recursive case
        return fib(n-1) + fib(n-2)  # O(2^n) time complexity due to exponential growth in recursive calls

print(fib(10))  
