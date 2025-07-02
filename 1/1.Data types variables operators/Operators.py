#Operators in Python

"""Python has a rich set of operators grouped by functionality:"""

#Arithmetic Operators
"""
Operator	Example	    Meaning
+	        a + b	    Addition
-	        a - b	    Subtraction
*	        a * b	    Multiplication
/	        a / b	    Division (float)
//	        a // b	    Floor division
%	        a % b	    Modulus (remainder)
**	        a ** b	     Exponentiation

"""

a = 9
b = 2

print("Addition:", a + b)        # 11
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 18
print("Division:", a / b)        # 4.5
print("Floor Division:", a // b) # 4
print("Modulus:", a % b)         # 1
print("Exponent:", a ** b)       # 81


#Assignment Operators

"""
Operator	Meaning
=	        Assign
+=	        Add and assign
-=	        Subtract and assign
*=	        Multiply and assign
/=	        Divide and assign

"""

#Example:

x = 10
print("Initial x:", x)

x += 5
print("After x += 5:", x)   # 15

x -= 3
print("After x -= 3:", x)   # 12

x *= 2
print("After x *= 2:", x)   # 24

x /= 4
print("After x /= 4:", x)   # 6.0


#Comparison (Relational) Operators

"""
Operator	Meaning
==	        Equal
!=	        Not equal
>	        Greater than
<	        Less than
>=	        Greater or equal
<=	        Less or equal


"""
#Example:

a = 10
b = 20

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


##Logical Operators
"""
Operator	Meaning	       Example
and	        Logical AND	   x > 5 and x < 10
or	        Logical OR	   x > 5 or x < 2
not	        Logical NOT	   not(x > 5)

"""

x = 7

# Logical AND
print(x > 5 and x < 10)  # True (7 > 5 and 7 < 10)

# Logical OR
print(x > 5 or x < 2)    # True (7 > 5 is True)

# Logical NOT
print(not(x > 5))        # False (x > 5 is True, not True → False)

#Bitwise Operators

"""Operate on binary numbers."""

"""
Operator	Meaning     	Example
&	        Bitwise AND	    a & b
`	`	    Bitwise OR
^	        Bitwise XOR	    a ^ b
~	        Bitwise NOT	    ~a
<<	        Left shift	    a << 2
>>	        Right shift	    a >> 2

"""
a = 10  # 0b1010
b = 4   # 0b0100

print("a & b:", a & b)    # 0
print("a | b:", a | b)    # 14
print("a ^ b:", a ^ b)    # 14
print("~a:", ~a)          # -11 (inverts bits, then adds negative)
print("a << 2:", a << 2)  # 40 (shifts left: 10 * 2^2)
print("a >> 2:", a >> 2)  # 2  (shifts right: 10 // 2^2)

'''🧠 Notes:
Bitwise operators work on integers only.

They're often used in low-level programming, flags, networking, and optimizations'''

# Membership Operators

"""
Operator	Meaning
in	        True if value is in sequence
not in	    True if value is not in sequence

"""

#Example:


"p" in "python"    # True
10 not in [1,2,3]  # True

#Identity Operators

"""
Operator	Meaning
is	        True if both refer to same object
is not	    True if they don't

"""
#Example:

a = [1,2,3]
b = a
a is b       # True (same object)
a == b       # True (same content)

#🧠 FAANG Python Interview Questions on Operators
'''🔸 1. What is the output of the following code?'''


a = 5
b = 2
print(a / b)
print(a // b)

#Concept: Division vs Floor Division
#Answer:

2.5     # float division
2       # floor division (drops decimal)

#🔸 2. What does this return and why?



print(3 < 2 < 1)

#Concept: Chained comparison
#Answer: False
#Explanation: Python evaluates it as:


'''(3 < 2) and (2 < 1) → False and False → False'''

#🔸 3. What is the output of this bitwise operation?


x = 5  # binary: 101
y = 3  # binary: 011
print(x & y)
print(x | y)
print(x ^ y)


1  # AND: 101 & 011 = 001
7  # OR : 101 | 011 = 111
6  # XOR: 101 ^ 011 = 110

#🔸 4. What will this code output?

x = 10
x += x - x * x
print(x)

#Concept: Operator precedence and assignment

'''x = 10 + 10 - 10 * 10 → 10 + 10 - 100 = -80'''

#🔸 5. Explain the difference between is and == with this example:

a = 256
b = 256
print(a is b)  # ?

a = 257
b = 257
print(a is b)  # ?

True   # Interned integers (Python caches -5 to 256)
False  # Different objects (not interned)

#🔸 6. What is the result and why?

a = [1, 2]
b = a
a += [3, 4]
print(a)
print(b)

[1, 2, 3, 4]
[1, 2, 3, 4]

#Why? += on lists is in-place modification (same reference)

#🔸 7. What is printed here?

print(True + True)
print(True * False)


2   # True is treated as 1
0   # False is treated as 0

#🔸 8. How does not affect evaluation here?


x = 5
print(not x > 3)

Answer: False

#Explanation: x > 3 → True → not True → False

#🔸 9. What will this print?

x = 0b1010  # 10 in binary
print(x << 2)
print(x >> 2)

40  # Left shift → 101000 (adds 2 zero bits)
2   # Right shift → 0010 (removes 2 bits)

#🔸 10. Does this raise an error?

print(10 / 0)

#Answer:
#✅ Yes, it raises: ZeroDivisionError: division by zero

#🔹 Bonus: Trick Question
#🔸 11. Predict the result

x = 1
x = x + (x == x)
print(x)

2  # Because x == x is True → True = 1 → x = 1 + 1 = 2
