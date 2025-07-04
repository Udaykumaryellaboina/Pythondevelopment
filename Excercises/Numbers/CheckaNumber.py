# Write a Python Program to Check if a Number is Positive, Negative or Zero.
def pnz(num:int):
    if num > 0:
        return "The Number is positive"
    elif num < 0:
        return "The Number is negative"
    else:
        return "the Number is Zero"
num=int(input("Enter the Number:"))
print(pnz(num))




# Write a Python Program to Check if a Number is Odd or Even.
def evenorodd(num:int):
    if num % 2 == 0:
        return "The Number  is even"
    else:
        return "The Number is ODD"
num = int(input("Enter the nUmber:"))
print(evenorodd(num))

# Write a Python Program to Check Leap Year
def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
year=input("Enter the year:")
if is_leap_year(year):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is NOT a Leap Year.")

#Write a Python Program to Check Prime Number

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check from 3 to √n, only odd numbers
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
"""Prime numbers don’t have divisors beyond their square root.
So instead of checking up to n, we check only up to √n.
int(n**0.5) + 1 gets us the integer value just above the square root.
We check only odd numbers (step size 2) — because even ones were already handled"""


# Example usage
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is NOT a Prime Number.")

# Input: Range from user
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"\nPrime numbers between {start} and {end}:")

for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=' ')


def is_prime_recursive(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime_recursive(n, i + 1)
