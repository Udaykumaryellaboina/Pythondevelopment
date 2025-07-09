#🔵 What is a while loop?
"The while loop is used to repeat a block of code as long as a condition is true."

#✅ 1. Basic Syntax

'''while condition:
    # block of code
The condition is checked before each iteration.

If it evaluates to True, the block runs.

If False, the loop ends.

✅ Example:'''

i = 1
while i <= 5:
    print(i)
    i += 1
'''Output:
1
2
3
4
5
'''

#✅ 2. Infinite
''''
A while loop without a condition that becomes False will 
loop forever (unless stopped manually or with break).

❌ Dangerous if not handled:

while True:
    print("This will run forever")
'''

#✅ 3. Using break in while Loop
'''Use break to exit the loop early based on a condition.'''

#✅ Example:

i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
'''Output:


1
2
3
4
'''

#✅ 4. Using continue in while Loop
"""Use continue to skip the rest of the current iteration and continue with the next one.

✅ Example:"""

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

'''Output:


1
2
4
5
'''

#✅ 5. while-else Block
"""The else block runs only if the loop completes normally (not via break).

✅ Example:"""

i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop finished")

"""Output:


1
2
3
Loop finished
If break is used, the else will not run.
"""

#✅ 6. Input-Based Loop
#Commonly used when reading input from the user until a condition is met.

#✅ Example:

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    print("You entered:", num)

#✅ 7. Countdown Timer Example

import time

count = 5
while count > 0:
    print(count)
    time.sleep(1)  # Waits 1 second
    count -= 1

print("Time's up!")

#✅ 8. Validating User Input

password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")

#✅ 9. Nested while Loops
"""One while inside another. Used for matrix traversal, pattern printing, etc."""


i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i}, {j})", end=' ')
        j += 1
    print()
    i += 1

'''Output:


(1, 1) (1, 2) (1, 3) 
(2, 1) (2, 2) (2, 3) 
(3, 1) (3, 2) (3, 3)'''

#✅ 10. Common Mistakes

#❌ Forgetting to update the loop variable:

i = 1
while i <= 5:
    print(i)
    # i += 1 is missing => Infinite loop!

#❌ Wrong condition:

"while i = 5:  # ❌ Error: use == not ="

#✅ Correct:

#while i == 5:

#✅ 11. Using Flags in while Loop

found = False
i = 0
nums = [1, 3, 5, 7]

while i < len(nums):
    if nums[i] == 5:
        found = True
        break
    i += 1

if found:
    print("Found!")
else:
    print("Not found")


#✅ Summary Table
'''
Concept	                Description
while	                Loop as long as condition is true
break	                Exit the loop immediately
continue	            Skip to next iteration
else with while	        Executes if loop finishes normally
Infinite loop	        while True – must be controlled manually
Input validation	    Keep prompting until valid input given
Nested while	        Used in grids/patterns
'''


#✅ 1. Reverse Digits of an Integer
#📌 Concept: Use while to extract digits and reverse


num = 12345
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

print("Reversed:", rev)

# Output: 54321

#✅ 2. Palindrome Number Check
#📌 Concept: Reverse number and compare to original

num = 121
original = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#✅ 3. Integer to Binary (without bin())


n = 10
binary = ""

while n > 0:
    binary = str(n % 2) + binary
    n //= 2

print("Binary:", binary)  # Output: 1010

#✅ 4. Find Square Root (Binary Search with while)
#📌 Concept: Use binary search with while to find sqrt


def sqrt(n):
    low, high = 0, n
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

print("Square root of 17:", sqrt(17))  # Output: 4 (integer part)

#✅ 5. Happy Number
#📌 Concept: Use while to repeatedly calculate sum of squares of digits


def isHappy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

print(isHappy(19))  # Output: True

#✅ 6. Fibonacci Series (Using While Loop)
#📌 Concept: Generate N Fibonacci numbers

n = 10
a, b = 0, 1
count = 0

while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1

#✅ 7. Power of Two
#📌 Concept: Repeated division using while


def isPowerOfTwo(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1

print(isPowerOfTwo(16))  # Output: True

#✅ 8. Length of Number (Digit Count)
#📌 Concept: Count number of digits using while


n = 123456
count = 0

while n > 0:
    n //= 10
    count += 1

print("Number of digits:", count)

#✅ 9. Armstrong Number
#📌 Concept: Sum of cubes of digits == number


num = 153
original = num
sum_val = 0

while num > 0:
    digit = num % 10
    sum_val += digit ** 3
    num //= 10

if sum_val == original:
    print("Armstrong number")
else:
    print("Not Armstrong")

#✅ 10. Remove Duplicates from Sorted List (Linked List)
#📌 Concept: while to iterate over nodes


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeDuplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head
