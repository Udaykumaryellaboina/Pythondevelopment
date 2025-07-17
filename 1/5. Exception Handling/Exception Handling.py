#🔹 What is an Exception?
'''An exception is an error that occurs during the execution of a program.
When an error occurs, Python interrupts the normal flow of the program and throws an exception.

Example:

a = 10 / 0  # ZeroDivisionError
🔹 Types of Errors
1. Syntax Errors (compile-time errors)
Occurs when Python can't understand the code due to incorrect syntax.

if True
    print("Hello")  # SyntaxError: Missing colon
2. Exceptions (Runtime Errors)
Occur during the execution of the program.
Examples: ZeroDivisionError, FileNotFoundError, IndexError, etc.'''

#🔹 Built-in Exception Types
'''Exception	                Meaning
ZeroDivisionError	        Dividing by zero
ValueError	                Invalid value for function
TypeError	                Wrong type used
IndexError	                List index out of range
KeyError	                Dictionary key not found
FileNotFoundError	        File doesn't exist
AttributeError	            Invalid object attribute
ImportError	                Module can't be imported
NameError	                Variable not defined
StopIteration	            No more items in iterator
MemoryError	                Out of memory'''

#🔹 Basic try and except

try:
    a = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

#✅ This prevents the program from crashing.

#🔹 try, except, else, and finally
'''📌 Structure:

try:
    # Code that may raise an exception
except SomeException:
    # Handle the exception
else:
    # Runs if there is no exception
finally:
    # Always runs (clean-up code)
✅ Example:'''

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Division by zero error!")
except ValueError:
    print("Invalid input. Enter a number.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")

#🔹 Handling Multiple Exceptions

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    # some code
except (ValueError, TypeError):
    print("Caught ValueError or TypeError")

#🔹 Accessing Exception Details

try:
    10 / 0
except ZeroDivisionError as e:
    print("Error occurred:", e)

#🔹 Catch All Exceptions (Not Recommended Always)
'''
try:
    # risky code
except Exception as e:
    print("Error:", e)
    '''
#🔹 Nested try-except

try:
    try:
        x = int("abc")
    except ValueError:
        print("Inner exception caught")
except Exception:
    print("Outer exception caught")

#🔹 Raising Exceptions Manually: raise
#You can manually throw an exception using raise.

age = -5
if age < 0:
    raise ValueError("Age cannot be negative")

#🔹 Creating Custom Exceptions

class MyCustomError(Exception):
    pass

raise MyCustomError("This is a custom error")

#You can also inherit from Exception and add custom behavior.
class NegativeValueError(Exception):
    def __init__(self, value):
        super().__init__(f"Negative value not allowed: {value}")
#🔹 assert Statement
#Used for debugging: if the condition is false, raises AssertionError.

x = -1
assert x >= 0, "x must be non-negative"

#🔹 with Statement and Exception Handling
#For auto-closing resources like files:

try:
    with open("file.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found.")
#🔹 Exception Chaining: raise from
try:
    1 / 0
except ZeroDivisionError as e:
    raise ValueError("Invalid value") from e

#🔹 Best Practices
'''Be specific in except blocks.
Avoid catching Exception unless necessary.
Always clean up resources with finally or with.
Use logging instead of print() in production.
Don't ignore exceptions silently.'''

#🔹 Example – Full Program

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Error:", e)
    else:
        print("Result:", result)
    finally:
        print("End of operation")

divide(10, 0)
divide(10, 2)

#🔹 Exception Hierarchy

'''BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      └── ...
You can catch a parent class (Exception) to catch its children.

🔹 When Not to Use Exceptions
Don’t use exceptions for control flow (like in loops).
Prefer checking conditions (like if file_exists) when possible.'''