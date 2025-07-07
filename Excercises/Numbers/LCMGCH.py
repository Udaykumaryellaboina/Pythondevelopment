import math

# Input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate GCD
gcd = math.gcd(num1, num2)

# Calculate LCM using formula: LCM = (num1 * num2) // GCD
lcm = (num1 * num2) // gcd

# Display the results
print(f"GCD of {num1} and {num2} is: {gcd}")
print(f"LCM of {num1} and {num2} is: {lcm}")

"""📌 Explanation:
math.gcd(a, b): Returns the greatest common divisor of a and b.
"""