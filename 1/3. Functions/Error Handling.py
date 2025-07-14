'''Error handling in Python is managed using exceptions.
When a Python program encounters an error during execution,
it raises an exception, which can be handled using special keywords.
If not handled, the program will crash.

Let's go step-by-step and cover all important error handling functions and concepts in Python:

🔹 1. try and except
Used to catch and handle exceptions.

try:
    # code that may raise an exception
except ExceptionType:
    # code to handle the exception
Example:'''

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a number.")

#🔹 2. else
"Used to define a block of code to be executed if no exception occurs in the try block."

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print(f"You entered {num}")

#🔹 3. finally
'''Used to define a block of code that always executes,
whether an exception occurs or not. Typically used for cleanup tasks 
(like closing files, connections, etc.)'''


try:
    f = open("file.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing the file.")
    f.close()

#🔹 4. raise
"Used to manually raise an exception."


age = -5
if age < 0:
    raise ValueError("Age cannot be negative.")

#You can also raise built-in exceptions or your own custom exceptions.

#🔹 5. assert
"Used to raise an exception if a condition is not met. Mainly used in debugging and testing."

x = 10
assert x > 0  # No error
assert x < 0, "x should be less than 0"  # Raises AssertionError

#🔹 6. Built-in Exception Classes
'''Python provides a rich hierarchy of built-in exceptions. Some commonly used are:
ZeroDivisionError
ValueError
TypeError
IndexError
KeyError
FileNotFoundError
ImportError
NameError
AttributeError
AssertionError
Each of these can be caught in except blocks.'''

#🔹 7. Catching Multiple Exceptions
"You can handle multiple exceptions in one block."

try:
    val = int("abc")
    res = 10 / 0
except (ValueError, ZeroDivisionError) as e:
    print("An error occurred:", e)

#🔹 8. Creating Custom Exceptions
"You can define your own exception class by inheriting from Exception."

class NegativeValueError(Exception):
    pass

value = -10
if value < 0:
    raise NegativeValueError("Negative value not allowed.")

"""
🔹 Summary Table
Keyword	   Purpose
try	       Wrap code that might raise exceptions
except	   Handle specific exceptions
else	   Run code only if no exception occurred
finally	   Run cleanup code regardless of exception
raise	   Manually trigger an exception
assert	   Debug-time checks that raise AssertionError

"""



#🔹 1. eval()
'''📌 Purpose:
Evaluates a Python expression (not a statement) given as a string and returns the result.

✅ Syntax:

eval(expression, globals=None, locals=None)
expression: A string containing a valid Python expression (like math, variable references, etc.).

globals (optional): Dictionary for global namespace.

locals (optional): Dictionary for local namespace.

✅ Example:
'''
x = 10
print(eval("x + 5"))  # Output: 15
print(eval("2 + 3 * 5"))  # Output: 17

'''⚠️ Warning:
eval() executes arbitrary code. Never use it with untrusted input.

# DANGEROUS!
user_input = "os.system('rm -rf /')"  # Don't do this
eval(user_input)  # This can delete files!'''

#🔹 2. exec()
'''📌 Purpose:
Executes any valid Python code — expressions, statements, function/class definitions — provided as a string.

✅ Syntax:

exec(code, globals=None, locals=None)
✅ Example:
'''
code = '''
for i in range(3):
    print("Hello", i)
'''
exec(code)
#You can even define functions dynamically:

exec("""
def greet(name):
    print("Hello", name)
""")
#greet("Alice")

''''🆚 eval() vs exec():
Feature	        eval()	                                     exec()
Input	        Only expressions	                       Any Python code (statements too)
Return value	Returns result	                           Returns None
Use case	    Simple evaluations	                       Dynamic code execution
'''

#🔹 3. compile()

'''📌 Purpose:
Converts a string of code into a code object that can be executed using eval() or exec().

✅ Syntax:

compile(source, filename, mode)
source: The code as a string.

filename: Just a name for the code (used in error messages).

mode: "eval" for expressions, "exec" for statements, "single" for single interactive statements.

✅ Example:'''

code_obj = compile("10 + 20", "<string>", "eval")
result = eval(code_obj)
print(result)  # Output: 30

code_obj = compile("for i in range(2): print(i)", "<string>", "exec")
exec(code_obj)

#🔐 Security Warning for All Three
'''These functions let you execute dynamic Python code. That can be extremely dangerous if:

You're executing user input without sanitization.

You're exposing internals of your application.

Always avoid using them in production unless absolutely necessary and you fully control the input.'''

'''🔚 Summary Table
Function	Description                                                Example Use Case
eval()	    Evaluates a Python expression as string	Dynamic            calculation: eval("a + b")
exec()	    Executes Python statements/code as string	               Running generated code blocks
compile()	Converts code string into code object	                   Precompile and reuse expressions'''