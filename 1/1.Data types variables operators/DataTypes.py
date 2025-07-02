#Data Types in Python
'''Python is a dynamically-typed language, 
which means you don’t need to declare the type of a variable explicitly. 
Data types are assigned at runtime.'''

#Basic Data Types
"""
| **Type**  | **Example**        | **Description**                    | **Common Operators / Usages**                         | **Example Code & Output**                         |
| --------- | ------------------ | ---------------------------------- | ----------------------------------------------------- | ------------------------------------------------- |
| `int`     | `10`, `-5`, `0`    | Integer numbers                    | `+`, `-`, `*`, `/`, `//`, `%`, `**`, `==`, `>`, `<`   | `5 + 3 → 8`<br>`10 // 3 → 3`<br>`4 ** 2 → 16`     |
| `float`   | `3.14`, `-0.01`    | Decimal numbers                    | All arithmetic + comparison                           | `3.5 * 2 → 7.0`<br>`5.0 / 2 → 2.5`                |
| `complex` | `3 + 4j`, `-2j`    | Complex numbers (real + imaginary) | `+`, `-`, `*`, `/`, `.real`, `.imag`                  | `(3 + 4j) * (1 - 2j) → 11 - 2j`                   |
| `bool`    | `True`, `False`    | Boolean values                     | `and`, `or`, `not`, `==`, `!=`, `+`, `*`              | `True + True → 2`<br>`False * 5 → 0`              |
| `str`     | `"Hello"`, `'abc'` | String of characters               | `+` (concatenation), `*`, `in`, `==`, slicing `[i:j]` | `"Hi" + "There" → "HiThere"`<br>`"a" * 3 → "aaa"` |

"""
# int
a = 10
b = 3
print(a + b)       # 13
print(a // b)      # 3 (floor division)
print(a % b)       # 1

# float
x = 5.5
print(x * 2)       # 11.0

# complex
z = 3 + 4j
print(z.real)      # 3.0
print(z.imag)      # 4.0

# bool
print(True + True)  # 2
print(False * 5)    # 0
print(not True)     # False

# str
#✅ Operators Supported by Strings in Python
'''
Operator	        Meaning	                    Example	              Output
+	                Concatenation	            "Hello" + "World"	"HelloWorld"
*	                Repetition	                "ha" * 3	        "hahaha"
==, !=	            Equality / Inequality	    "abc" == "abc"	       True
<, >, <=, >=	    Lexicographic comparison	"apple" < "banana"	   True
in	                Substring check	            "app" in "apple"	   True
not in	            Not a substring	            "dog" not in "cat"	   True

'''

#❌ Operators NOT Supported on Strings
'''
Operator	                  Meaning	        Example	      
-, /, %, **, //, &, `	`	 Not valid for str	"a" - "b"
'''
'''
🧠 FAANG Tip:
Use "x" in string instead of find() for clean and Pythonic code.

Remember, string comparison is case-sensitive and lexicographic ("Z" < "a").
'''
# Concatenation
print("Hello" + " " + "World")  # Hello World

# Repetition
print("ha" * 3)                 # hahaha

# Equality
print("abc" == "abc")          # True
print("abc" != "ABC")          # True

# Lexicographic Comparison
print("apple" < "banana")      # True
print("Zoo" > "apple")         # False

# Membership
print("a" in "banana")         # True
print("z" not in "apple")      # True

#✅ Lexicographic Comparison in Python

"""
Lexicographic comparison is how strings are compared in dictionary 
order (like in a phonebook or lexicon).

In Python, string comparisons using <, >, <=, >= follow 
lexicographic (alphabetical) order, based on the Unicode (ASCII) value of characters.

📚 Rules of Lexicographic Comparison
Character by character comparison from left to right.

The first pair of characters that differ determines the result.

Shorter strings can be "less" if all characters match up to that length.

Uppercase letters come before lowercase ones (because ord('A') < ord('a')).

📌 Examples:"""

print("apple" < "banana")     # ✅ True (because 'a' < 'b')

print("cat" > "car")          # ✅ True ('t' > 'r')

print("Zoo" < "apple")        # ✅ True (Z=90 < a=97)

print("abc" < "abcd")         # ✅ True (shorter string is less if prefix matches)

print("Dog" > "dog")          # ❌ False ('D'=68 < 'd'=100)

#🔍 Behind the Scenes (using ord())

print(ord('A'))  # 65
print(ord('Z'))  # 90
print(ord('a'))  # 97
print(ord('z'))  # 122

#"Zebra" < "apple"  → True

#because ord('Z') = 90 < ord('a') = 97

"""💡 Tip for Interviews
Lexicographic order is case-sensitive in Python.

Use .lower() or .casefold() for case-insensitive comparisons:

"""

print("Zoo".lower() < "apple".lower())  # False

# Collection Data Types
"""
Type	  Example	            Description
list	  [1, 2, 3]	            Ordered, mutable, allows duplicates
tuple	  (1, 2, 3)	            Ordered, immutable, allows duplicates
set	      {1, 2, 3}	            Unordered, unique elements
dict	  {"name": "Alice"}	    Key-value pairs, unordered

"""

#✅ Python list Basics
#🔹 Definition

my_list = [1, 2, 3, 'apple', [4, 5]]
#✅ Ordered (maintains insertion order)

#✅ Mutable (can change items)

#✅ Allows duplicates

#✅ Can be nested

#🧰 Common Built-in Methods of Lists
#Here’s a categorized list of commonly used list methods:
'''
Method	            Description	                                                        Example
append(x)	        Adds x to the end of the list	                                    lst.append(5)
extend(iterable)	Adds all elements from another iterable (like a list, tuple)        lst.extend([6, 7])
insert(i, x)	    Inserts x at index i	                                            lst.insert(1, 'apple')
remove(x)	        Removes first occurrence of x	                                    lst.remove('apple')
pop([i])	        Removes and returns item at index i (last item if i not given)	    lst.pop()
clear()	            Removes all items from the list                                 	lst.clear()
index(x[, start])	Returns the index of first occurrence of x	                        lst.index(3)
count(x)	        Counts how many times x appears	                                    lst.count(2)
sort()	            Sorts the list in place (ascending by default)	                    lst.sort()
reverse()	        Reverses the list in place	                                        lst.reverse()
copy()	            Returns a shallow copy of the list	                                new_list = lst.copy()

📌 Examples'''

lst = [3, 1, 4, 1, 5]

lst.append(9)        # [3, 1, 4, 1, 5, 9]
lst.extend([2, 6])   # [3, 1, 4, 1, 5, 9, 2, 6]
lst.insert(2, 7)     # [3, 1, 7, 4, 1, 5, 9, 2, 6]
lst.remove(1)        # [3, 7, 4, 1, 5, 9, 2, 6]
value = lst.pop()    # 6 (removed), lst now: [3, 7, 4, 1, 5, 9, 2]
idx = lst.index(9)   # 5
cnt = lst.count(1)   # 1
lst.sort()           # [1, 2, 3, 4, 5, 7, 9]
lst.reverse()        # [9, 7, 5, 4, 3, 2, 1]

"""🧠 Tips
Use sorted(lst) if you want a new sorted list without modifying the original.

Use copy() or slicing (lst[:]) to make copies and avoid reference issues.

Lists can store mixed data types, but doing so may cause issues with sorting or arithmetic."""


#✅ What is a Tuple in Python?
'''A tuple is:

An ordered collection

Immutable (cannot be changed after creation)

Allows duplicates

Can contain mixed data types

Defined using parentheses ()

🔹 Example:'''

t = (1, 2, 3, 2, 'apple')

'''

🧠 Key Properties
Property	        Supported by Tuples?	     Example
Ordered	            ✅ Yes	Indexable:           t[0] → 1
Immutable	        ✅ Yes                    	 t[0] = 10 → ❌ TypeError
Allows Duplicates	✅ Yes	                     (1, 2, 2, 3) is valid
Nesting Allowed  	✅ Yes	                     (1, [2, 3], (4, 5))

🧰 Built-in Tuple Methods
Tuples have only 2 built-in methods, because they are immutable:

Method	Description	Example	Output
count(x)	Counts how many times x appears	t.count(2)	2
index(x)	Returns first index of x	t.index('apple')	4

📌 Example Code'''

t = (1, 2, 3, 2, 'apple')

print(t[0])           # 1
print(t[-1])          # 'apple'
print(t.count(2))     # 2
print(t.index('apple'))  # 4


#🔍 Immutability: What You Can’t Do

t[1] = 10     # ❌ TypeError: 'tuple' object does not support item assignment
t.append(5)   # ❌ AttributeError: 'tuple' object has no attribute 'append'

'''📦 Workaround for Modification
Tuples are immutable, but you can:

'''
t = (1, 2, 3)
t = list(t)
t.append(4)
t = tuple(t)
print(t)  # (1, 2, 3, 4)

#🔁 Tuple Unpacking

a, b, c = (1, 2, 3)
print(a, b, c)  # 1 2 3

#🔸 When to Use a Tuple?
'''Use tuples when:

You want read-only or fixed data

Used as dictionary keys (lists can't be keys)

For returning multiple values from a function

🧪 FAANG-Level Interview Tip:
They might test immutability with nested structures:'''

t = (1, [2, 3])
t[1][0] = 99   # ✅ This is allowed! The tuple is immutable, but the list inside it is not.
print(t)       # (1, [99, 3])



#✅ What is a set in Python?

'''A set is:

Unordered: No indexing, elements appear in arbitrary order.

Unindexed

Unique elements only: Duplicates are automatically removed.

Mutable: You can add/remove elements.

Defined with curly braces {} or set().

🔹 Example:'''

s = {1, 2, 3, 2, 1}
print(s)  # Output: {1, 2, 3}

'''
🧠 Key Features
Feature	            Supported?	          Example
Unordered	        ✅ Yes	              {3, 2, 1} may display in any order
Unique values only	✅ Yes	              {1, 1, 2} → {1, 2}
Mutable	            ✅ Yes	              You can .add() or .remove()
Mixed types allowed	✅ Yes	              {1, 'apple', 3.5}
No duplicates allowed	✅Yes	          Automatically removed
'''

#🧰 Built-in Set Methods
"""
Method	                  Description	                                    Example
add(x)	                  Add element x	                                    s.add(4)
remove(x)	              Remove element x (raises error if not found)	    s.remove(2)
discard(x)	              Remove x if present (no error if not)	            s.discard(100)
pop()	                  Remove and return a random element	            s.pop()
clear()	                  Remove all elements	                            s.clear()
copy()	                  Shallow copy of set	                            t = s.copy()
union(set2)	              Return union (all unique elements)	            s.union(t) or `s
intersection(set2)	      Common elements	                                s & t
difference(set2)	      Elements in s but not in t	                    s - t
symmetric_difference(set2)	Elements in either s or t but not both	        s ^ t
issubset(set2)	          Check if s is subset of t	                        s.issubset(t)
issuperset(set2)	      Check if s is superset of t	                    s.issuperset(t)
isdisjoint(set2)	      True if sets have no elements in common	        s.isdisjoint(t)
update(set2)	          Add elements from another set                  	s.update(t)

📌 Example Code:"""

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1.union(s2))         # {1, 2, 3, 4, 5}
print(s1 & s2)              # {3}
print(s1 - s2)              # {1, 2}
print(s1 ^ s2)              # {1, 2, 4, 5}

s1.add(10)
s1.discard(2)
print(s1)                   # {1, 3, 10}

#🔍 Notes
#Use set() to create an empty set.


s = set()  # ✅
s = {}     # ❌ creates an empty dict

#set does not support indexing or slicing (unlike list/tuple).

#Elements must be hashable (e.g., cannot add a list or dict).

#🧠 FAANG-Level Trick Example

s = {1, 2, 3}
t = {2, 3, 4}
s &= t  # Same as: s = s.intersection(t)
print(s)  # {2, 3}


#✅ What is a dict in Python?

"""A dictionary is:

A collection of key-value pairs

Unordered in versions < 3.7, but insertion-ordered in Python 3.7+

Mutable (can add, update, delete entries)

Keys must be unique and hashable

Values can be of any data type

🔹 Example"""

person = {"name": "Alice", "age": 30, "is_student": False}
'''

🧠 Key Features
Property	            Example	                              Explanation
Keys must be unique	    {"a": 1, "a": 2} → {"a": 2}	          Last value overwrites earlier
Keys must be hashable	dict({[1,2]: "list"})                 ❌ Error	Lists can't be keys
Access by key	        person["name"] → "Alice"	           Direct lookup
Mutable	                person["age"] = 31	                   You can change values
'''

'''
🧰 Built-in Dictionary Methods

Method	                       Description	                                                    Example
get(key[, default])        	Return value of key, return default if not found	                d.get("x", 0)
keys()	                    Return view of all keys	                                            d.keys()
values()	                Return view of all values	                                        d.values()
items()	                    Return view of (key, value) pairs	                                d.items()
update(dict2)	            Add/update entries from another dictionary	                        d.update({"x": 1})
pop(key[, default])       	Remove specified key and return value	                            d.pop("x", "Not Found")
popitem()	                Remove and return the last inserted (key, value) pair	            d.popitem()
clear()	                    Remove all items	                                                d.clear()
copy()	                    Return a shallow copy	                                            d2 = d.copy()
setdefault(k[, v])	        Get value of k, insert if not found	                               d.setdefault("z", 100)
fromkeys(iterable, value)	Create new dict with keys from iterable & same value	           dict.fromkeys(["a", "b"], 0)

📌 Example Code
'''
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(person["name"])           # Alice
print(person.get("gender", "N/A"))  # N/A

person["age"] = 26
person["gender"] = "Female"

print(person.keys())            # dict_keys(['name', 'age', 'city', 'gender'])
print(person.values())          # dict_values(['Alice', 26, 'New York', 'Female'])

person.pop("city")              # Removes 'city'
print(person)

person.update({"job": "Engineer"})
print(person)

d2 = person.copy()
print(d2)

person.clear()
print(person)  # {}

#🔄 Dictionary Comprehension

squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#🔒 Immutable Keys Only
#Valid keys:


{"a": 1, 10: "x", (1, 2): "tuple"}

#Invalid key:

{[1, 2]: "list"}  # ❌ TypeError: unhashable type: 'list'


#🧠 FAANG Tip:
#Use .get() and .setdefault() for safe lookups and default initialization in loops:


d = {}
for ch in "banana":
    d[ch] = d.get(ch, 0) + 1
print(d)  # {'b': 1, 'a': 3, 'n': 2}
