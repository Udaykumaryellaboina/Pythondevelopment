#🔷 What is Memory Management in Python?
'''Python uses automatic memory management that includes:
Reference Counting
Garbage Collection
Memory Pooling (pymalloc)
Interning for immutable objects
Python tries to handle memory efficiently and safely,
but provides tools to monitor or control it when needed.'''

#🔹 1. id() – Object Identity / Memory Address
'''📌 Purpose:
Returns the unique identity (memory address) of an object during its lifetime.
✅ Syntax:
id(object)
✅ Example:'''

x = 10
y = 10
print(id(x))  # Same as id(y), because integers are interned
print(id(y))

#For mutable objects, the id() changes if you create a new object.

a = [1, 2, 3]
print(id(a))     # e.g., 140509231145600
a.append(4)
print(id(a))     # Same ID — list modified in place

#🔹 2. hash() – Hash Value of an Object
'''📌 Purpose:
Returns the hash value of an object (integer). Hashes are used in:
Dictionaries (as keys)
Sets
Hashing algorithms
✅ Syntax:
hash(object)
Only immutable (hashable) types can be hashed: int, str, tuple, etc.
Mutable types like list, dict, etc., cannot be hashed.
✅ Example:'''

print(hash("hello"))     # Output: an integer hash
print(hash(123))         # Output: 123 (same as value)

#❌ Invalid:

# hash([1, 2, 3]) → TypeError: unhashable type: 'list'

#🔹 3. sys.getsizeof() – Size in Memory (in Bytes)
'''📌 Purpose:
Returns the memory size (in bytes) of an object.
✅ Syntax:
import sys
sys.getsizeof(object)
✅ Example:'''

import sys
x = 1000
print(sys.getsizeof(x))  # Output: varies (e.g., 28 bytes for small int)

#🔹 4. gc Module – Garbage Collector
'''📌 Purpose:
Control the automatic garbage collector for cleaning up unused objects.'''

import gc

gc.collect()           # Trigger GC manually
gc.get_count()         # See generation counts
gc.get_threshold()     # Get GC threshold

#🔹 5. tracemalloc Module – Track Memory Allocations
'''📌 Purpose:
Trace where memory is being allocated.
✅ Example:'''

import tracemalloc
tracemalloc.start()
x = [i for i in range(10000)]
current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current} bytes; Peak: {peak} bytes")
tracemalloc.stop()

# 6. del Statement – Remove Reference
'''Deletes a variable reference — useful for 
    manually freeing memory (if no other references exist).'''


a = [1, 2, 3]
del a  # The list can now be garbage collected

#🔹 7. memoryview() – Efficient Binary Memory Handling
#Used for efficient access to binary data like bytes and bytearrays without copying.


data = bytearray(b'hello')
mv = memoryview(data)
print(mv[0])   # 104 (ASCII of 'h')

'''✅ Summary Table
Function / Module	Purpose
id(obj)	            Returns identity (memory address) of object
hash(obj)	        Returns hash (only for immutable objects)
sys.getsizeof(obj)	Size of object in memory (bytes)
del var	            Deletes a reference to an object
gc	                Garbage collection control
tracemalloc	        Tracks memory allocations
memoryview()	     Efficient binary data access (no copy)

🧠 Key Concepts Recap
id() = Identity (like memory address)
hash() = Used in sets/dictionaries
sys.getsizeof() = Size in bytes
gc module = Control garbage collection
tracemalloc = Profile memory usage
del = Remove reference
memoryview = Work with memory directly (zero-copy)'''

