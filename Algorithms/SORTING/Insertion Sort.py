"""🔹 What is Insertion Sort?
Insertion Sort is a simple sorting algorithm inspired by how we arrange playing cards in our hand.
👉 Imagine picking cards one by one and inserting each card in its correct 
position relative to already sorted cards in your hand.

Steps:

Start from the second element (because a single element is already sorted).

Compare it with the elements before it.

Shift the elements greater than the current element to the right.

Insert the current element in the correct position.

Repeat until the list is sorted.

🔹 Insertion Sort Algorithm in Python"""
def insertion_sort(arr):
    # Traverse from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]   # current element to insert
        j = i - 1      # index of the previous element

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key in its correct position
        arr[j + 1] = key

    return arr


# Example usage
data = [12, 11, 13, 5, 6]
print("Original:", data)
print("Sorted:", insertion_sort(data))


"""✅ Output:

Original: [12, 11, 13, 5, 6]
Sorted: [5, 6, 11, 12, 13]

🔹 Dry Run Example

Input: [12, 11, 13, 5, 6]

Pass 1: [11, 12, 13, 5, 6]

Pass 2: [11, 12, 13, 5, 6] (already in correct place)

Pass 3: [5, 11, 12, 13, 6]

Pass 4: [5, 6, 11, 12, 13]

🔹 Time Complexity of Insertion Sort

Best Case (Already Sorted) → O(n)
(Only one comparison per element, no shifting.)

Worst Case (Reverse Sorted) → O(n²)
(Each element compared with all previous ones.)

Average Case → O(n²)
(Roughly half of elements are compared and shifted.)

🔹 Space Complexity

O(1) (In-place sorting, only uses a few extra variables.)

🔹 Comparison with Other Sorting Algorithms
Algorithm	          Best Case	Average Case	Worst Case	Space Complexity	Stable?
Insertion Sort	      O(n)	    O(n²)	    O(n²)	    O(1)	        ✅ Yes
Bubble Sort	        O(n)	    O(n²)	    O(n²)	    O(1)	        ✅ Yes
Selection Sort	    O(n²)	    O(n²)	    O(n²)	    O(1)	        ❌ No
Merge Sort	        O(n log n)	O(n log n)	O(n log n)	O(n)	        ✅ Yes
Quick Sort	        O(n log n)	O(n log n)	O(n²)	    O(log n)	    ❌ No (in some cases)
Heap Sort	        O(n log n)	O(n log n)	O(n log n)	O(1)	        ❌ No
🔹 Why use Insertion Sort?

Simple and easy to implement.

Efficient for small arrays or partially sorted arrays.

Useful in real-time when new data keeps coming in (online sorting).

Not suitable for large datasets because of O(n²) time."""