#🔷 What Are Sequences in Python?
'''A sequence is an ordered collection of elements,
where each element is assigned an index (starting from 0).

✅ Common Sequence Types:
List → []
Tuple → ()
String → "abc"
Range → range(start, stop)
Bytes → b'abc'
Bytearray

🔶 Sequence Functions and Operations
Python provides built-in functions that work with all sequence types:'''

#✅ 1. len() – Length of a sequence

len("hello")      # 5
len([1, 2, 3])    # 3

#✅ 2. min() / max() – Minimum or Maximum element

min([5, 3, 8])    # 3
max("abcde")      # 'e'

#✅ 3. sum() – Sum of all elements (for numeric sequences)

sum([1, 2, 3])    # 6

#✅ 4. sorted() – Returns a sorted list

sorted((3, 1, 2))    # [1, 2, 3]

#✅ 5. reversed() – Returns a reverse iterator

list(reversed([1, 2, 3]))  # [3, 2, 1]

#✅ 6. enumerate() – Adds index to elements

for i, v in enumerate(['a', 'b']):
    print(i, v)

# Output: 0 a, 1 b
#✅ 7. zip() – Combine multiple sequences element-wise

list(zip([1, 2], ['a', 'b']))  # [(1, 'a'), (2, 'b')]
#✅ 8. all() / any() – Boolean checks

all([True, 1, 'abc'])     # True
any([0, '', None, 3])     # True

#✅ 9. list(), tuple(), str() – Convert between sequence types

tuple("abc")     # ('a', 'b', 'c')
list((1, 2))     # [1, 2]
str([1, 2, 3])   # '[1, 2, 3]'

#✅ 10. range(start, stop, step) – Immutable sequence of numbers

list(range(1, 5))  # [1, 2, 3, 4]

#🔶 Sequence Methods (on list, string, etc.)
'''📘 Lists:
append(), extend(), insert(), remove(), pop(), index(), count(), sort(), reverse(), copy()
📘 Strings (also a sequence!):
upper(), lower(), strip(), find(), replace(), split(), join()
🔶 Common Sequence Operations
Operation	    Example     	Result
Indexing	    s[0]	        First element
Slicing	        s[1:3]	        Subsequence
Concatenation	s + t	        Combines two
Repetition	    s * 3	        Repeat sequence
Membership	    'a' in 'apple'	True
Iteration	    for item in s:	Loop items

✅ Summary Table of Sequence Functions
Function	       Description
len()	           Number of items
min() / max()      Smallest/largest element
sum()	           Sum of numeric elements
sorted()	       Sorted copy
reversed()	       Reverse iterator
enumerate()	       Index + item pairing
zip()	           Combine multiple sequences
all() / any()	   Logical check on all/any items
list(), tuple()	   Convert to desired sequence type'''