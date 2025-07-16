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



