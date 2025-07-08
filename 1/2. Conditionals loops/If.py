#✅ 1. What is an if Statement?
"The if statement is used to execute a block of code only if a specified condition is True."

#🧠 Syntax:
'''
if condition:
    # block of code to execute if condition is true
'''
#✅ 2. Basic Example of if

age = 18
if age >= 18:
    print("You are eligible to vote.")

'''age >= 18 is the condition

If True, print() will run.

If False, it will be skipped.
'''
#✅ 3. if-else Statement
'''Use else to provide an alternative block of code when the condition is False.'''


age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#✅ 4. if-elif-else Ladder
'''Used when you have multiple conditions to test.'''

marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

'''Checks one condition after another until one is True.

Once one condition is satisfied, remaining conditions are skipped.
'''

#✅ 5. Nested if Statements
'''An if statement inside another if statement.'''

age = 25
citizen = True

if age >= 18:
    if citizen:
        print("You can vote.")
    else:
        print("Only citizens can vote.")
else:
    print("You are too young to vote.")

#✅ 6. Logical Operators in if Conditions#
#🔹 and: All conditions must be True

age = 20
has_id = True

if age >= 18 and has_id:
    print("Access granted.")

#🔹or: At least one condition must be True

is_admin = False
is_owner = True

if is_admin or is_owner:
    print("Access granted.")

#🔹 not: Negates the condition

logged_in = False

if not logged_in:
    print("Please log in first.")

#✅ 7. Comparison Operators in if
'''
Operator	Meaning          	Example
==	        Equal to	        a == b
!=	        Not equal to	    a != b
>	        Greater than	    a > b
<	        Less than	        a < b
>=	        Greater or equal	a >= b
<=	        Less or equal	    a <= b
'''

#✅ 8. Truthy and Falsy Values in if
"""
In Python, the following are considered Falsy:
0
None
False
'' (empty string)
[], {}, () (empty collections)
Everything else is Truthy
"""

name = ""

if name:
    print("Hello", name)
else:
    print("Name is empty.")

#✅ 9. if with Functions

def is_even(n):
    return n % 2 == 0

num = 6

if is_even(num):
    print("Even number")
else:
    print("Odd number")


#✅ 10. Ternary (One-line) if Expression
#🧠 Syntax:

#result = value_if_true if condition else value_if_false

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

#✅ 11. Common Mistakes in if Conditions
#❌ Wrong indentation

'''if x > 10:
print("Too big")  # ❌ IndentationError'''
#✅ Correct:
x=10
if x > 10:
    print("Too big")

#❌ Using = instead of == in condition

'''if x = 10:  # ❌ SyntaxError
✅ Correct:'''

if x == 10:
    print(x)

#✅ 12. Real-world Practice Examples
#🔸 Even or Odd Checker

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#🔸 Leap Year Checker

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#📘 Summary Table
'''
Concept	                  Description
if	                      Runs block if condition is True
if-else	                  Adds fallback block
if-elif-else	          Chain of conditions
Nested if	              if inside if
Logical operators	      Combine multiple conditions (and, or, not)
Comparison operators	  Used to compare values
Ternary/Conditional Expr	One-line if-else
Truthy/Falsy values	Empty = False, non-empty = True
'''




#✅ 1.Classic if - else Based

#🔹 Even or Odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#🔹 Check Leap Year

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#🔹 Find the Largest of Three Numbers

a, b, c = 5, 9, 3
if a >= b and a >= c:
    print("a is largest")
elif b >= a and b >= c:
    print("b is largest")
else:
    print("c is largest")

#✅ 2. Digit / Number

#🔹 Check Armstrong Number

num = 153
original = num
sum_val = 0

while num > 0:
    digit = num % 10
    sum_val += digit ** 3
    num //= 10

if sum_val == original:
    print("Armstrong Number")
else:
    print("Not Armstrong")

#🔹 Palindrome Number

num = 121
original = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#🔹 FizzBuzz(FAANG Favorite)

n = 15
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#✅ 3. String - based If Condition Problems
#🔹 Check Anagram

s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not anagram")


#🔹 Check Palindrome String

s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

#✅ 4. Edge Case + Conditions in Loops
#🔹 Check Prime Number

n = 13
if n <= 1:
    print("Not Prime")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

#🔹 Print All Prime Numbers in Range

for num in range(2, 50):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

#🔹 Compare Two Version Numbers

v1 = "1.0.2"
v2 = "1.0.10"


def compare_versions(v1, v2):
    a = list(map(int, v1.split('.')))
    b = list(map(int, v2.split('.')))

    max_len = max(len(a), len(b))
    a += [0] * (max_len - len(a))
    b += [0] * (max_len - len(b))

    for i in range(max_len):
        if a[i] < b[i]:
            return -1
        elif a[i] > b[i]:
            return 1
    return 0


print(compare_versions(v1, v2))  # Output: -1

#🔹 Password Strength Checker

password = "Admin@123"

if len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isupper() for c in password) and any(
        c in "!@#$%^&*()" for c in password):
    print("Strong Password")
else:
    print("Weak Password")
