#🔷 1. ord() – Unicode Code Point of a Character
'''📌 Purpose:
Returns the Unicode code point (integer value) of a given character.
✅ Syntax:
ord(character)
✅ Example:'''

print(ord('A'))   # Output: 65
print(ord('a'))   # Output: 97
print(ord('₹'))   # Output: 8377

#Used when you need to convert characters to their Unicode integer representation.
#🔷 2. chr() – Character from Unicode Code Point
'''📌 Purpose:
Returns the character corresponding to an integer Unicode code point.
✅ Syntax:
chr(number)
✅ Example:'''

print(chr(65))    # Output: 'A'
print(chr(97))    # Output: 'a'
print(chr(8377))  # Output: '₹'
#It is the reverse of ord().

#🔷 3. format() – Advanced String Formatting
'''📌 Purpose:
Used to insert values into a string using placeholders {}.

✅ Syntax:
"{}".format(value)
"{name}".format(name="Alice")
✅ Examples:
Positional formatting:'''

print("Hello, {}".format("Alice"))           # Output: Hello, Alice
print("Sum of {} and {} is {}".format(2, 3, 5))  # Output: Sum of 2 and 3 is 5
#Named placeholders:

print("Name: {name}, Age: {age}".format(name="John", age=30))
#Number formatting:

print("Pi is approximately {:.2f}".format(3.14159))  # Output: Pi is approximately 3.14
#format() is very flexible for string construction and number formatting.
#Newer alternative: f-strings (Python 3.6+) → f"Name: {name}"

#🔷 4. repr() – Printable/Official String Representation
'''📌 Purpose:
Returns a string that would yield the same object when passed to eval(), 
or gives a more unambiguous representation (often used for debugging).
✅ Syntax:
repr(object)
✅ Examples:'''

s = 'Hello\nWorld'
print(s)            # Output: Hello (newline) World
print(repr(s))      # Output: 'Hello\nWorld'

x = 5
print(repr(x))      # Output: '5'

#repr() shows the string with escape characters, unlike print() or str().

'''🔚 Summary Table
Function	Description	                                             Example
ord('A')	Returns Unicode                                         code point of 'A'	65
chr(65)  	Returns character for                                   Unicode code point 65	'A'
format()	Formats strings using placeholders {}	                "Hello {}".format("John")
repr(obj)	Returns official, debug-friendly string representation	repr("Hi\nBye") → 'Hi\\nBye'''''