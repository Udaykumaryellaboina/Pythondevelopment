# Write a program that will take three digits from the user and add the square of each digit.
# Input three-digit number
num = int(input("Enter a 3-digit number: "))

# Extract each digit using % and //
digit1 = num // 100             # First digit
digit2 = (num // 10) % 10       # Second digit
digit3 = num % 10               # Third digit

# Calculate square of each and add
square_sum = digit1**2 + digit2**2 + digit3**2

print("Sum of squares of digits:", square_sum)

# Write a program that will check whether the number is armstrong number or not.
'''An Armstrong number is one whose sum of digits raised to the power three equals the
number itself. 371, for example, is an Armstrong number because 3**3 + 7**3 + 1**3 =
371.'''
# Armstrong number: sum of cubes of each digit equals the number

num = int(input("Enter a 3-digit number: "))

# Extract digits
digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10

# Cube each digit and add
cube_sum = digit1**3 + digit2**3 + digit3**3

# Check Armstrong
if num == cube_sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

#:Write a program that will take user input of (4 digits number) and check whether the number
# is narcissist number or not.
# Input a 4-digit number
num = int(input("Enter a 4-digit number: "))

# Extract digits manually
d1 = num // 1000             # Thousands place
d2 = (num // 100) % 10       # Hundreds
d3 = (num // 10) % 10        # Tens
d4 = num % 10                # Ones

# Calculate each digit raised to power 4 and sum
power_sum = d1**4 + d2**4 + d3**4 + d4**4

# Check Narcissistic
if num == power_sum:
    print(f"{num} is a narcissistic number.")
else:
    print(f"{num} is not a narcissistic number.")
