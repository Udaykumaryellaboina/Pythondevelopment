#🔍 Linear Search Algorithm in Python
"""
Definition:
Linear Search (also called Sequential Search) is the simplest search algorithm that
checks every element in a list one by one until the desired element is found or the list ends.

✅ Characteristics:
Feature	Description
Time Complexity	O(n) — checks each element once
Space Complexity	O(1) — no extra space needed
Best Case	O(1) — if the target is at the beginning
Worst Case	O(n) — if the target is at the end or not found
Data Requirement	Works on unsorted or sorted lists

🧠 How It Works:
Start from index 0.
Compare each element with the target.
If match found, return index or element.
If not found after checking all elements, return -1 or "Not found".
🧪 Python Example:"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # return the index of the found element
    return -1  # target not found

# Example usage
numbers = [5, 3, 7, 1, 9, 2]
target = 1

result = linear_search(numbers, target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")
#🧾 Output:

#Element found at index: 3
'''
📌 When to Use Linear Search?
When the dataset is small.
When the list is unsorted.
When performance is not critical.'''
