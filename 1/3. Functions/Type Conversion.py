'''In Python, type conversion (also known as type casting) is
the process of converting one data type into another.
Python provides both implicit and explicit type conversion.'''

#🔷 1. Implicit Type Conversion (Automatic)
'''Python automatically converts smaller data types to larger data types
when needed — for example, from int to float.

✅ Example:'''

a = 5      # int
b = 2.5    # float
c = a + b  # Python converts `a` to float automatically
print(c)   # Output: 7.5
print(type(c))  # Output: <class 'float'>

#✅ No data loss or error.

#🔶 2. Explicit Type Conversion (Manual)
#You manually convert one type to another using built-in conversion functions.

#🔹 Common Type Conversion Functions
'''Function	   Converts To	      Example
int()	       Integer	          int('10') → 10
float()	       Floating Point	  float('3.14') → 3.14
str()	       String	          str(123) → '123'
bool()	       Boolean	          bool(0) → False
list()	       List	              list('abc') → ['a','b','c']
tuple()        Tuple	          tuple([1,2,3]) → (1,2,3)
set()	       Set	              set([1,2,2]) → {1,2}
dict()	       Dictionary	      dict([(1,'a'),(2,'b')]) → {1:'a', 2:'b'}
complex()	   Complex number	  complex(2, 3) → (2+3j)
chr()	       Character	      chr(65) → 'A'
ord()	       Unicode code point ord('A') → 65
bin()	       Binary string	  bin(10) → '0b1010'
oct()	       Octal string	      oct(10) → '0o12'
hex()	       Hex string	      hex(10) → '0xa'
bytes()	       Bytes object    	  bytes("abc", "utf-8")
bytearray()	   Mutable bytes	  bytearray("abc", "utf-8")
memoryview()   Memory view	      memoryview(b"abc")
frozenset()	   Immutable set	  frozenset([1,2,3])'''

#🔸 Examples of Each:
int()

int('10')     # 10
int(3.99)     # 3
float()

float('3.14') # 3.14
float(5)      # 5.0
str()

str(123)      # '123'
str(True)     # 'True'
bool()

bool(0)       # False
bool('abc')   # True
list()

list('abc')            # ['a', 'b', 'c']
list((1, 2, 3))         # [1, 2, 3]
tuple()

tuple([1, 2, 3])        # (1, 2, 3)
set()

set([1, 2, 2, 3])       # {1, 2, 3}
dict()

dict([(1, 'a'), (2, 'b')])  # {1: 'a', 2: 'b'}
complex()

complex(2, 3)           # (2+3j)
chr() and ord()

chr(65)        # 'A'
ord('A')       # 65
bin(), oct(), hex()

bin(10)        # '0b1010'
oct(10)        # '0o12'
hex(10)        # '0xa'
bytes() and bytearray()

bytes("abc", "utf-8")       # b'abc'
bytearray("abc", "utf-8")   # bytearray(b'abc')
memoryview()

memoryview(b"abc")          # <memory at 0x...>
frozenset()

frozenset([1, 2, 3])        # frozenset({1, 2, 3})

#🔐 Notes:
#If the input is not valid for conversion, Python raises a ValueError or TypeError.


int("abc")     # ValueError
list(123)      # TypeError

'''✅ Summary Table
Source \ Target	int()	float()	str()	bool()
"123"	        ✅	     ✅	    ✅	    ✅
123.45	        ✅	     ✅  	✅	    ✅
True	        ✅	     ✅ 	✅	    ✅
"abc"	        ❌	     ❌ 	✅	    ✅'''

