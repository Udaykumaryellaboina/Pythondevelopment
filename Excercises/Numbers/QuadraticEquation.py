# Write a Python program to solve quadratic equation

import cmath  # For complex number support

# Get coefficients from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
d = (b**2) - (4*a*c)

# Find two solutions using the quadratic formula
root1 = (-b + cmath.sqrt(d)) / (2 * a)
root2 = (-b - cmath.sqrt(d)) / (2 * a)

# Display the results
print(f"The solutions are: {root1} and {root2}")
