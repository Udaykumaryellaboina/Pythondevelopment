# Write a Python Program to Find the Factorial of a Number.

def factorial(number:int):
    if number<0:
        return "enter  a  positive number"
    elif number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(5))


def factorial_iterative(n):
    if n < 0:
        return "Invalid input"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
