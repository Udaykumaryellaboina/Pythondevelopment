#🔷 1. Built-in Math Functions (No Import Needed)
'These functions are available without importing any module.'

#✅ abs(x) – Absolute value

print(abs(-5))  # Output: 5

#✅ pow(x, y) – x raised to the power y (same as x**y)

print(pow(2, 3))  # Output: 8

#✅ round(x, n) – Round x to n decimal places
print(round(3.14159, 2))  # Output: 3.14

#✅ min() and max() – Minimum or maximum value

print(min(5, 3, 7))  # Output: 3
print(max(5, 3, 7))  # Output: 7

#🔷 2. math Module Functions (Need import math)
#You need to import the math module to use these.

import math

''''🔹 Common math functions:
Function	         Description	                             Example
math.sqrt(x)	     Square root of x	                         math.sqrt(16) → 4.0
math.pow(x, y)	     x raised to the power y (float result)	     math.pow(2, 3) → 8.0
math.floor(x)	     Rounds down to nearest integer              math.floor(3.7) → 3
math.ceil(x)	     Rounds up to nearest integer	             math.ceil(3.2) → 4
math.fabs(x)	     Absolute value as float	                 math.fabs(-3) → 3.0
math.factorial(x)	 Factorial of x	                             math.factorial(5) → 120
math.gcd(x, y)	      Greatest Common Divisor	                 math.gcd(12, 8) → 4
math.lcm(x, y)	Least Common Multiple (Python 3.9+)	             math.lcm(3, 4) → 12
math.isqrt(x)	       Integer square root	                     math.isqrt(10) → 3'''

'''🔷 3. Trigonometric Functions
Function	    Description	                               Example
math.sin(x)	    Sine of x (in radians)	                   math.sin(math.pi/2) → 1.0
math.cos(x)	    Cosine of x	                               math.cos(0) → 1.0
math.tan(x)	    Tangent of x	                           math.tan(math.pi/4) → 1.0
math.degrees(x)	Convert radians to degrees	               math.degrees(math.pi) → 180
math.radians(x)	Convert degrees to radians	               math.radians(180) → π

🔷 4. Logarithmic and Exponential Functions
Function	     Description	         Example
math.log(x)    	Natural log (base e)	   math.log(10)
math.log10(x)	Base-10 logarithm	       math.log10(100) → 2.0
math.log2(x)	Base-2 logarithm	       math.log2(8) → 3.0
math.exp(x)	    e raised to the power x	   math.exp(1) → 2.718...

🔷 5. Constants in math Module
Constant	Value
math.pi	    3.141592653589793 (π)
math.e	    2.718281828459045 (e)
math.tau	6.283185307179586 (2π)
math.inf	Infinity (float('inf'))
math.nan	Not a number (float('nan'))'''

#🔷 6. Random Numbers (via random module, bonus info)
import random

print(random.randint(1, 10))    # Random integer from 1 to 10
print(random.random())

# Random float between 0 and 1

''''✅ Summary Table
Category	          Examples
Built-in	          abs(), pow(), round(), min(), max()
Arithmetic	          math.sqrt(), math.floor(), math.ceil()
Trigonometry	      math.sin(), math.cos(), math.tan()
Log/Exp	              math.log(), math.exp()
Constants	           math.pi, math.e, math.inf'''

