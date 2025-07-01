#Variabl es in Python

#What is a Variable?

"""A variable is a name that refers to a value stored in memory.

A variable in Python is a container for storing data values. 

You can think of it as a label attached 
to a value that you can use and change throughout your program.

"""

x = 10       # x is a variable holding an integer
name = "Raj" # name is a variable holding a string
x = 5        # integer
name = "Uday"  # string
pi = 3.14    # float
is_valid = True  # boolean

#💡 Key Points:

"""
No need to declare a type.

Case-sensitive (name ≠ Name)

Variable name can include letters, digits, and underscores, but must start with a letter or underscore.

"""

#🔹 Rules for Naming Variables

"""Must begin with a letter (A–Z or a–z) or an underscore (_)

Cannot start with a number

Can only contain letters, numbers, and underscores

Case-sensitive (Age and age are different)

Cannot use Python reserved keywords like if, else, for, class, etc.

"""

#🔹 Dynamic Typing

"""
Python is dynamically typed – you don’t need to declare the type of the variable. 

Python infers the type at runtime."""

a = 10        # a is int
a = "hello"   # now a is str

#❌ Invalid Variable Names:

1name = "John"     # starts with a number ❌
#0utput:SyntaxError: invalid decimal literal
my-name = "Raj"    # hyphen is not allowed ❌
# Output:SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?


#Variable Reassignment

x = 5
x = "Hello"   # Now x refers to a string instead of an integer

# Multiple Assignment

a, b, c = 1, 2, 3
x = y = z = 100


#🔹 Swapping Variables

a, b = 10, 20
a, b = b, a

print(a, b)  # Output: 20 10

#🔹 Global and Local Variables

x = 50  # global variable

def func():
    x = 10  # local variable
    print(x)

func()        # Output: 10
print(x)      # Output: 50


"""To modify the global variable inside a function, use global:"""

x=123
def update():
    global x
    x = 999
    print(x)
update()        # Output: 999
print(x)        ## Output: 999

#🔹 Type Checking

x = 42
print(type(x))  # Output: <class 'int'>


#✅ Type Safety in Python Variables

"""
Type safety means ensuring that variables are used only in ways that are consistent with their data types.
 While Python is dynamically typed, it is not statically type-safe like Java or C
 . However, Python does offer ways to improve type safety, especially in modern Python (3.5+).
 
 """

#🔹 1. Dynamic Typing (Low Type Safety)

"""
In Python, you don’t need to declare variable types explicitly. 
You can reassign a variable to a different type freely.

"""

x = 10       # int
x = "hello"  # now x is str — no error!

"🔸 This flexibility is powerful but can lead to runtime errors."

#🔹 2. Type Errors at Runtime

"""Python doesn't catch type mismatches at compile time:"""


a = "5"
b = 2
print(a + b)  # ❌ TypeError: can only concatenate str (not "int") to str

#🔹 3. Improving Type Safety with Type Hints

"""Python 3.5+ introduced type hints (annotations):"""

def greet(name: str) -> str:
    return "Hello " + name

greet(123)  # ❌ No error at runtime, but tools like mypy will warn you
greet("uday") #output = 'Hello uday'
greet(uday) # name 'uday' is not defined

#✔️ Use tools like mypy to statically check types:


'''mypy script.py'''

#🔹 4. Using isinstance() for Runtime Checks

x = 42
if isinstance(x, int):
    print("x is an integer")
    
#NOTE:if x is of any other type onterh in int it wil not give any output or error
#output: x is an integer

x = "udat"
if isinstance(x, str):
    print("x is an string")
#NOTE:if x is of any other type onterh in str it wil not give any output or error  
  
#🔹 5. Type Safety in Collections (With typing)

from typing import List, Dict

def total(scores: List[int]) -> int:
    return sum(scores)


#🔹 6. Enforcing Type Safety with pydantic or dataclasses

"""Use dataclasses or pydantic for stricter type-safe models:"""


from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float

item = Product("Book", 99.99)
print(item)
#Product(name='Book', price=99.99)
print(type(Product))
#<class 'type'>
print(type(item))


#output <class '__main__.Product'>

###FAANG-Level Variable Questions in Python

"""❓ 1. What will be the output of the following code?"""

def append_to_list(val, my_list=[]):
    my_list.append(val)
    return my_list

print(append_to_list(1))
print(append_to_list(2))
print(append_to_list(3))

#Concept tested: Mutable default arguments

#Expected Output:


[1]
[1, 2]
[1, 2, 3]

"""
Explanation: my_list retains the reference to the same list across function calls — mutable 
default arguments are only evaluated once.
"""

#❓ 2. What is the output and why?

x = 10
def foo():
    print(x)
    x = 5

foo()


#Concept tested: Variable shadowing and UnboundLocalError

"""
UnboundLocalError: local variable 'x' referenced before assignment
Explanation: Inside the function, x is treated as a local variable because it's assigned to. 
So when print(x) tries to access it before the assignment, it raises an error."""

###❓ 3. What will be printed?

a = [1, 2, 3]
b = a
a += [4, 5]

print(a)
print(b)

#Concept tested: Mutability and object references

#Output:

[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]

##Explanation: a += [...] modifies the list in-place, so b reflects the same change.

#❓ 4. Closures and Variable Capture

functions = []
for i in range(3):
    def f():
        return i
    functions.append(f)

results = [func() for func in functions]
print(results)

#Concept tested: Late binding in closures

#Output:


[2, 2, 2]

"""Explanation: All functions capture the same variable i, which ends at 2."""

#✅ Fix with default arguments:


functions = []
for i in range(3):
    def f(i=i):
        return i
    functions.append(f)

#❓ 5. Global vs Nonlocal Example

x = 5
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
        print(x)
    inner()
    print(x)
outer()

#Concept tested: nonlocal variable scoping

#Output:
11
11

"""Explanation: nonlocal x refers to x in the outer() scope (not global)."""

#❓ 6. Swapping variables without temp

a = 5
b = 10
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)

"""Concept tested: Bitwise variable manipulation"""

#Output:


10 5

#❓ 7. Variable ID & Interning

a = 256
b = 256
print(a is b)

a = 257
b = 257
print(a is b)

"""Concept tested: Variable interning (Python caches small integers)"""

#Output:


True
False

#❓ 8. Function Default and Mutable Class Attribute

class MyClass:
    vals = []

    def __init__(self, val):
        self.vals.append(val)

a = MyClass(1)
b = MyClass(2)
print(a.vals)
print(b.vals)

#Output:


[1, 2]
[1, 2]



"""Explanation: vals is a class-level variable (shared across all instances)."""



#1. Mutable vs Immutable Types

"""Immutable types: int, float, str, tuple, bool"""

x = 5
y = x
x = 10

print(y)  # 5 (y not affected)

"""Mutable types: list, dict, set, bytearray"""


a = [1, 2]
b = a
a.append(3)
print(b)  # [1, 2, 3] (b reflects the change)

"""
📌 FAANG Twist: Changing an immutable type creates a new object. 
With mutable types, you modify the same object in memory.
"""

#🔷 2. Default Argument Pitfalls

"""Using mutable default arguments causes shared state across function calls."""

def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] ❌ Unexpected behavior

#✅ Fix:


def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
print(add_item(1))  # [1]
print(add_item(2)) #[2]

#🔷 3. Variable Scope – global, nonlocal, local

x = 10

def outer():
    x = 20
    def inner():
        nonlocal x
        x += 1
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()

#Output:


Inner: 21
Outer: 21

"""
local: Inside current function

nonlocal: Closest enclosing non-global scope

global: Refers to top-level variable

"""

#🔷 4. Closures and Late Binding

"""Functions can capture variables from their surrounding scope."""


funcs = []
for i in range(3):
    def f():
        return i
    funcs.append(f)

print([f() for f in funcs])  # [2, 2, 2]

"""🔍 What You Might Expect:
You might think the output will be:

[0, 1, 2]

But the actual output is:


[2, 2, 2]

✅ Why? — Closures + Late Binding
f() is a closure, meaning it remembers the variable i from the surrounding scope.

BUT: it doesn’t capture the current value of i at the time of creation.

Instead, it refers to i when the function is actually called, which is after 
the loop ends, and i becomes 2 (the last value in range(3)).

So, all 3 functions in the funcs list return 2 when called.

🔁 What Actually Happens:

# After the loop ends, i = 2

funcs[0]() → returns i → 2  
funcs[1]() → returns i → 2  
funcs[2]() → returns i → 2
Hence:


[2, 2, 2]
"""

#✅ Fix with early binding:

funcs = []
for i in range(3):
    def f(i=i):  # 👈 bind current value of i
        return i
    funcs.append(f)

print([f() for f in funcs])  # ✅ Output: [0, 1, 2]


funcs = []
for i in range(3):
    def f(i=i+1):  # 👈 bind current value of i
        return i
    funcs.append(f)

print([f() for f in funcs])  # ✅ Output: [1,2,3]

funcs = []
def f():
    for i in range(3):
        funcs.append(f)
   # 👈 bind current value of i
        return i

print([f() for f in funcs])  # ✅ Output: []

#🔷 5. Object References and Memory IDs
"""Use id() to get the memory address."""


x = [1, 2, 3]
y = x
print(id(x) == id(y))  # True (same object)



x = x + [4]

print(id(x) == id(y))  # False (new object created)

'''📌 In-place operations (+=, append) mutate; non-in-place create new objects.'''

##🔷 6. Python Interning (Strings & Small Integers)

"""Python caches:

Small integers: -5 to 256

Common strings"""

a = 256
b = 256
print(a is b)  # True (interned)

a = 257
b = 257
print(a is b)  # False (not interned)

#Concept: Python Interning / Object Caching

'''Python automatically caches (interns) some immutable objects like:

Small integers: from -5 to 256

Some strings (depending on usage)

This means that for values in that range, Python reuses the same object in memory to optimize performance.

🔍 Explanation:
a = 256 and b = 256
Both a and b point to the same memory address because Python reuses the object for small integers:


print(id(a))  # e.g. 140715116170320
print(id(b))  # same as id(a)
print(a is b)  # ✅ True
a = 257 and b = 257
257 is outside the interned range, so Python creates two different objects:


print(id(a))  # e.g. 140715115877904
print(id(b))  # different from id(a)
print(a is b)  # ❌ False

🔁 is vs ==
is: checks if two variables refer to the same object in memory

==: checks if values are the same


a = 257
b = 257
print(a == b)  # ✅ True (values are equal)
print(a is b)  # ❌ False (different memory addresses)

📌 Don’t rely on is for value equality. Use == instead.
'''


#🔷 7. Deepcopy vs Shallow Copy

import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)      # Shallow copy
c = copy.deepcopy(a)  # Deep copy

a[0][0] = 999
print(b)  # [[999, 2], [3, 4]] ❌
print(c)  # [[1, 2], [3, 4]] ✅

'''Shallow copy: Copies outer list, shares inner objects

Deep copy: Recursively copies all nested objects

'''

#🔷 8. Class vs Instance Variables

class A:
    shared = []

    def __init__(self, val):
        self.shared.append(val)

a = A(1)
b = A(2)

print(a.shared)  # [1, 2] ✅ shared

#To make it instance-specific:

class A:
    def __init__(self, val):
        self.unique = []
        self.unique.append(val)

"""
Concept	Common               Mistake / Trap	                                                  Example
🔸 Mutable default args	   Shared state across function calls	                              python\ndef add(val, lst=[]):\n lst.append(val)\n return lst\n\nprint(add(1)) # [1]\nprint(add(2)) # [1, 2] ❌\n
🔸 Closures	               Late binding captures final loop value	                          python\nfuncs = []\nfor i in range(3):\n def f(): return i\n funcs.append(f)\n\nprint([f() for f in funcs]) # [2, 2, 2] ❌\n
🔸 global / nonlocal	   Misunderstanding of variable scope	                              python\nx = 10\n\ndef foo():\n print(x) # ❌ UnboundLocalError\n x = 5\n\nfoo()\n
🔸 is vs ==	               Using is for value comparison	                                  python\na = 1000\nb = 1000\nprint(a == b) # ✅ True\nprint(a is b) # ❌ False (not same object)\n
🔸 Object copying	       Expecting copy() to recursively clone	                          python\nimport copy\na = [[1, 2], [3, 4]]\nb = copy.copy(a)\na[0][0] = 99\nprint(b) # [[99, 2], [3, 4]] ❌\n
🔸 Class variables	       Believing they are instance-specific	                              python\nclass A:\n shared = []\n def __init__(self, x):\n self.shared.append(x)\n\nA(1)\nA(2)\nprint(A.shared) # [1, 2] ❌\n
"""