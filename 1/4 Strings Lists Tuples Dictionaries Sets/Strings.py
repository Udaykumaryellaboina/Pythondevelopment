
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


#📋 Categorized String Methods with Examples
''''✅ 1. Case Conversion Methods
Method	          Description	                  Example
lower()	          Converts to lowercase	           'HELLO'.lower() → 'hello'
upper()	          Converts to uppercase	           'hello'.upper() → 'HELLO'
title()	          Capitalizes each word	           'hello world'.title() → 'Hello World'
capitalize()	  Capitalizes first character	   'python'.capitalize() → 'Python'
swapcase()	      Swaps case	                   'PyThOn'.swapcase() → 'pYtHoN'
casefold()	      Aggressive lowercasing	       'Straße'.casefold() → 'strasse' '''

#✅ 2. Search and Check Methods
'''Method	           Description	                   Example
find(sub)	        First index or -1	              'hello'.find('l') → 2
rfind(sub)	        Last index or -1	              'hello'.rfind('l') → 3
index(sub)	        Like find(), but raises error	   'hello'.index('e') → 1
rindex(sub)	        Like rfind(), but raises error	   'hello'.rindex('l') → 3
startswith(prefix)	Checks start	                   'hello'.startswith('he') → True
endswith(suffix)	Checks end	                       'hello'.endswith('o') → True
in	Check           if substring exists	               'ell' in 'hello' → True
'''


#✅ 3. Check for Type of String Content
'''Method	    Description	           Example
isalpha()	Only letters	        'abc'.isalpha() → True
isdigit()	Only digits	            '123'.isdigit() → True
isalnum()	Letters and digits	    'abc123'.isalnum() → True
isspace()	Only whitespace        	' '.isspace() → True
islower()	All lowercase	        'hello'.islower() → True
isupper()	All uppercase	        'HELLO'.isupper() → True
istitle()	Title case	            'Hello World'.istitle() → True'''

#✅ 4. Modification and Formatting Methods
'''Method	            Description                    	Example
strip()   	        Remove spaces from both ends	' hi '.strip() → 'hi'
lstrip()	        Remove left spaces	            ' hi'.lstrip() → 'hi'
rstrip()	        Remove right spaces	            'hi '.rstrip() → 'hi'
replace(old, new)	Replace substring	            'hello'.replace('l', 'x') → 'hexxo'
split()	            Split by space or separator	    'a,b,c'.split(',') → ['a', 'b', 'c']
rsplit()	        Split from right	            'a,b,c'.rsplit(',', 1) → ['a,b', 'c']
splitlines()	    Split on newlines	            'a\nb\nc'.splitlines() → ['a', 'b', 'c']
join(iterable)	    Join items with string	        '-'.join(['a', 'b']) → 'a-b' '''

#✅ 5. Alignment Methods
'''Method	        Description	            Example
center(width)	Centers string	         'hi'.center(5) → ' hi '
ljust(width)	Left-aligns string	     'hi'.ljust(5) → 'hi '
rjust(width)	Right-aligns string	     'hi'.rjust(5) → ' hi'
zfill(width)	Pad with zeros	         '42'.zfill(5) → '00042'''''

#✅ 6. Count and Encoding
'''Method	        Description	             Example
count(sub)	    Number of occurrences	'banana'.count('a') → 3
encode()	    Encode to bytes	         'hello'.encode() → b'hello'
format()	    String formatting	     "My name is {}".format("John") → 'My name is John'
format_map()	Formatting with dict	 "{name}".format_map({'name': 'Alice'}) → 'Alice'''''

#✅ 7. Testing Identifiers and Printable
'''Method	        Description	           Example
isidentifier()	Valid variable name	   'my_var'.isidentifier() → True
isprintable()	Printable characters   'hello!'.isprintable() → True'''

#✅ 8. Others
'''Method	           Description	        Example
maketrans()	        Mapping table	    str.maketrans("ae", "12")
translate(table)	Apply mapping	    'apple'.translate(str.maketrans("ae", "12")) → '1ppl2'''''

##🔄 Summary
'''Case Methods: lower(), upper(), title(), capitalize(), swapcase(), casefold()
Search: find(), rfind(), index(), startswith(), endswith()
Check: isalpha(), isdigit(), isalnum(), islower(), etc.
Format/Replace: replace(), split(), join(), format()
Alignment: center(), ljust(), rjust(), zfill()
Count/Translate: count(), encode(), translate()'''

