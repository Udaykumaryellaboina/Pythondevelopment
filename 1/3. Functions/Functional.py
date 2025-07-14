#🔷 What is Functional Programming?
'''In Functional Programming, we:
Avoid changing states and mutable data
Use pure functions
Focus on what to do, not how to do it
Make heavy use of functions like map(), filter(), reduce(), and lambda expressions

🔹 Key Functional Programming Functions in Python
Here are the most commonly used functional programming tools in Python:'''

#✅ 1. map()
'''Applies a function to every item in an iterable (like a list) 
and returns a map object (which can be converted to list).

📌 Syntax:

map(function, iterable)
✅ Example:'''

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # Output: [1, 4, 9, 16]

#✅ 2. filter()

'''Filters elements from an iterable for which a function returns True.
📌 Syntax:
filter(function, iterable)
✅ Example:'''

nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # Output: [2, 4, 6]

#✅ 3. reduce() (from functools module)
'''Applies a function cumulatively to items in an iterable, reducing it to a single value.

📌 Syntax:

from functools import reduce
reduce(function, iterable)
✅ Example:
'''
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 24

#✅ 4. lambda Functions (Anonymous Functions)
'''A short, one-line function that doesn't require a name.

📌 Syntax:
lambda arguments: expression
✅ Example:'''

square = lambda x: x**2
print(square(5))  # Output: 25

#You often use lambda with map(), filter(), reduce().

#✅ 5. all() and any()
'''all() returns True if all elements in an iterable are true.
any() returns True if any one element is true.

✅ Example:'''

nums = [1, 2, 3, 0]
print(all(nums))  # False, because 0 is false
print(any(nums))  # True, because at least one number is true

#✅ 6. zip() and enumerate() (Common in FP)
#zip() – Combine two or more iterables:

a = [1, 2, 3]
b = ['a', 'b', 'c']
print(list(zip(a, b)))  # [(1, 'a'), (2, 'b'), (3, 'c')]
#enumerate() – Add index to an iterable:

colors = ['red', 'green', 'blue']
for i, color in enumerate(colors):
    print(i, color)

#✅ 7. Higher-Order Functions
#A function that takes another function as an argument or returns a function.

#✅ Example:

def apply_func(f, x):
    return f(x)

print(apply_func(lambda x: x**2, 4))  # Output: 16

#✅ 8. Pure Functions
'''A pure function:
Has no side effects (does not change external state)
Always gives the same output for the same input

✅ Example:'''

def add(a, b):
    return a + b  # Pure function


''''🔚 Summary Table
Function	  Purpose
map()	      Transform each item in an iterable
filter()	  Keep items that satisfy a condition
reduce()	  Reduce items to a single result
lambda	      Write small anonymous functions
all()	      Check if all values are true
any()	      Check if any value is true
zip()	      Combine iterables element-wise
enumerate()	   Add indexes to iterables'''
