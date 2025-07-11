#🔍 What is Binary Search?
'''Binary Search is an efficient algorithm used to find a specific
element in a sorted list. It works by dividing the search space in half again and again,
reducing the time it takes to find the item.
'''

#✅ Prerequisite
'''The list must be sorted in ascending order (very important).
Binary search is more efficient than linear search, especially for large lists.
'''

#💡 Idea
'''Suppose you are looking for a number in a book that contains sorted page numbers. 
Instead of going page by page, you:
'''
'''
Open the book in the middle.
Check if it's the page you're looking for.
If not, decide whether to go left (lower numbers) or right (higher numbers).
Repeat until you find the page.
This is what binary search does in code.
'''

#🔁 Steps (Algorithm)

'''Start with the left and right pointers at the start and end of the list.
While left is less than or equal to right:
Calculate the middle index.
Compare the target with the middle element:
If equal → Found the item.
If target < middle element → Search in the left half.
If target > middle element → Search in the right half.
If the item is not found, return -1 or "Not Found".'''


#🧠 Time Complexity

'''Best case: O(1) → Found in the middle.
Worst case: O(log n) → Keep dividing the list in half.
Space: O(1)'''

#🐍 Python Code with Detailed Comments

def binary_search(arr, target):
    # Step 1: Initialize pointers
    left = 0                 # Start of the list
    right = len(arr) - 1     # End of the list

    # Step 2: Repeat the loop until left crosses right
    while left <= right:
        # Step 3: Find the middle index
        mid = (left + right) // 2   # Integer division to get the middle index

        # Step 4: Check the value at mid
        if arr[mid] == target:
            return mid  # Found the target, return the index

        # Step 5: Decide where to search next
        elif target < arr[mid]:
            right = mid - 1  # Target is in the left half
        else:
            left = mid + 1   # Target is in the right half

    # Step 6: If not found, return -1
    return -1
#🔎 Example

# List must be sorted
numbers = [2, 4, 6, 8, 10, 12, 14]
target = 10

# Call the function
result = binary_search(numbers, target)

# Output result
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

#Output:
#Element found at index 4
#🧪 Dry Run (Step-by-Step)
'''Let’s say:


arr = [2, 4, 6, 8, 10], target = 8
left = 0, right = 4

mid = (0 + 4) // 2 = 2, arr[mid] = 6

8 > 6 → search right → left = 3

mid = (3 + 4) // 2 = 3, arr[mid] = 8

8 == 8 → FOUND!

🚫 What if the list is unsorted?

arr = [10, 4, 6, 2, 8]
Binary search will give wrong results. Always sort the list first!
📌 Bonus: Python version with recursion

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

# Example
arr = [1, 3, 5, 7, 9]

print(binary_search_recursive(arr, 7, 0, len(arr) - 1))  # Output: 3

✅ Summary
Step	Action
1	Check if the list is sorted
2	Set left and right pointers
3	Loop until left <= right
4	Check middle value
5	Narrow the search (left or right half)
6	Return index if found or -1
'''