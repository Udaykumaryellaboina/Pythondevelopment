# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

# Input a 4-digit number
num = int(input("Enter a 4-digit number: "))

# Convert to string and reverse it
reverse_num = int(str(num)[::-1])

print(f"Reversed number is: {reverse_num}")

# Check if the reverse is the same
if num == reverse_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")


def reverse_number(num, rev=0):
    if num == 0:
        return rev
    else:
        return reverse_number(num // 10, rev * 10 + num % 10)

# Input from user
number = int(input("Enter a 4-digit number: "))
reversed_number = reverse_number(number)

print(f"Reversed number is: {reversed_number}")

# Check if the number is a palindrome
if number == reversed_number:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

#Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

# Input any integer
num = int(input("Enter an integer: "))

print("Digits in reverse order:")
while num > 0:
    digit = num % 10       # Get the last digit
    print(digit, end=' ')  # Print with space
    num = num // 10        # Remove the last digit
