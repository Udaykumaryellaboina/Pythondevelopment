#🔷 1. What is an Iterator in Python?
'''An iterator is an object that allows you to loop through a
collection (like a list, tuple, string, etc.) one element at a time.
To be an iterator, an object must:
Implement the __iter__() method (returns the iterator object itself)
Implement the __next__() method (returns the next element, or raises StopIteration)'''

#✅ Example: Using an Iterator

nums = [1, 2, 3]
it = iter(nums)       # Create an iterator

print(next(it))       # Output: 1
print(next(it))       # Output: 2
print(next(it))       # Output: 3
# print(next(it))     # Raises StopIteration

#🔶 iter() Function
'''📌 Purpose:
Returns an iterator from a sequence (like list, tuple, string, etc.).
✅ Example:'''

colors = ['red', 'green', 'blue']
it = iter(colors)
print(next(it))  # red

#🔶 next() Function
'''📌 Purpose:
Returns the next item from the iterator. Raises StopIteration when there are no more items.
✅ Example:'''

names = iter(['Alice', 'Bob'])
print(next(names))  # Alice
print(next(names))  # Bob

# next(names) would raise StopIteration
#🔷 2. What is a Generator?
'''A generator is a simpler way to create iterators using:
A function with the yield keyword
Or generator expressions (like list comprehensions but with ())

✅ Benefits of Generators:
Memory-efficient (don’t store all items in memory)
Used for lazy evaluation (generate items on-the-fly)

✅ Generator Function Example'''

def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(3)
print(next(gen))  # 3
print(next(gen))  # 2
print(next(gen))  # 1
# next(gen) raises StopIteration

#✅ Generator Expression Example

squares = (x*x for x in range(5))
print(next(squares))  # 0
print(next(squares))  # 1

#🔶 Difference Between Iterator and Generator
'''Feature	Iterator	                                Generator
Definition	Class with __iter__() and __next__()	Function with yield
Memory usage	Can be large (stores all values)	Memory-efficient (lazy evaluation)
Simplicity	More complex	                        Simpler and cleaner'''

#🔷 3. range() Function – Built-in Sequence Generator
'''range() is a built-in immutable sequence used for looping a fixed number of times.
📌 Syntax:
range(start, stop, step)
start: beginning value (default = 0)
stop: end value (exclusive)
step: increment (default = 1)

✅ Examples:'''

for i in range(5):         # 0 to 4
    print(i)

print(list(range(1, 6)))   # [1, 2, 3, 4, 5]
print(list(range(5, 0, -1))) # [5, 4, 3, 2, 1]
#✅ Properties of range():
'''It's not a list; it's a lazy iterable
Supports len(), in, slicing

🔶 Summary Table
Function	Purpose
iter()	    Creates an iterator from an iterable
next()	    Gets next item from iterator/generator
yield	    Pauses generator, returns a value
range()	    Creates a memory-efficient sequence

✅ Final Comparison
Concept	Type	    Memory Usage	            Reusability	      Syntax
Iterator	Object	High (if storing values)	Yes	              iter(), next()
Generator	         Function or Expr	         LowOne-time use   yield
range()	             Immutable seq	Very Low	Yes	               range()'''
