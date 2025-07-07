#Write a Python Program to Print the Fibonacci sequence.

#iterative
def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n): #i goes from 0 to n-1.
        print(a, end=' ')
        a, b = b, a + b

#recursive

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Print first n terms
for i in range(10):
    print(fibonacci_recursive(i), end=' ')

"""Method	Time	Space	Notes
Recursion	O(2ⁿ)	O(n)	Simple but slow
Iterative	O(n)	O(1)	Fast and memory efficient"""