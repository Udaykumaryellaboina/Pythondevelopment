#Variables in Python

#What is a Variable?
"""A variable is a name that refers to a value stored in memory."""

x = 10       # x is a variable holding an integer
name = "Raj" # name is a variable holding a string

#💡 Key Points:
"""
No need to declare a type.

Case-sensitive (name ≠ Name)

Variable name can include letters, digits, and underscores, but must start with a letter or underscore."""

#❌ Invalid Variable Names:

1name = "John"     # starts with a number ❌
my-name = "Raj"    # hyphen is not allowed ❌


#Variable Reassignment

x = 5
x = "Hello"   # Now x refers to a string instead of an integer

# Multiple Assignment

a, b, c = 1, 2, 3
x = y = z = 100
