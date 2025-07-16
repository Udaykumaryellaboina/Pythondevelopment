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

