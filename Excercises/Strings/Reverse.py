#✅ 1. Using String Slicing (Most Pythonic Way)

s = "hello"
reversed_s = s[::-1]
print(reversed_s)  # Output: "olleh"

#✅ 2. Using reversed() and join()
s = "hello"
reversed_s = ''.join(reversed(s))
print(reversed_s)  # Output: "olleh"

#✅ 3. Using a Loop (Manual Reversal)
s = "hello"
reversed_s = ""
for char in s:
    reversed_s = char + reversed_s
print(reversed_s)  # Output: "olleh"

#✅ 4. Using Recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

s = "hello"
print(reverse_string(s))  # Output: "olleh"

#✅ 5. Using Stack (List as Stack)
s = "hello"
stack = list(s)
reversed_s = ""
while stack:
    reversed_s += stack.pop()
print(reversed_s)  # Output: "olleh"
#✅ 6. Using List Comprehension
s = "hello"
reversed_s = ''.join([s[i] for i in range(len(s)-1, -1, -1)])
print(reversed_s)  # Output: "olleh"
#✅ 7. Using while Loop and Index
s = "hello"
reversed_s = ""
i = len(s) - 1
while i >= 0:
    reversed_s += s[i]
    i -= 1
print(reversed_s)  # Output: "olleh"

#✅ 8. Using reduce() from functools
from functools import reduce

s = "hello"
reversed_s = reduce(lambda x, y: y + x, s)
print(reversed_s)  # Output: "olleh"

#✅ 9. Using map() with reversed() (Unusual but works)
s = "hello"
reversed_s = ''.join(map(str, reversed(s)))
print(reversed_s)  # Output: "olleh"

#✅ 10. Using a Lambda Function

reverse = lambda s: s[::-1]
print(reverse("hello"))  # Output: "olleh"
