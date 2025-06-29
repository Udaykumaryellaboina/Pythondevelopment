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

x = 5
x += 3   # x = x + 3 → x = 8


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
print(a > b)  # False

##Logical Operators
"""
Operator	Meaning	       Example
and	        Logical AND	   x > 5 and x < 10
or	        Logical OR	   x > 5 or x < 2
not	        Logical NOT	   not(x > 5)

"""

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

