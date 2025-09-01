

# Merge Sort – Explanation and Code


## 🔹 What is Merge Sort?

"""Merge Sort is a **divide and conquer algorithm** used for sorting.

It works by **dividing the array into smaller sub-arrays**, sorting them recursively,
 and then **merging the sorted sub-arrays** to produce the final sorted array.

---

## 🔹 How Merge Sort Works (Step by Step)

1. **Divide:** Split the array into two halves (left and right).
2. **Conquer:** Recursively sort the two halves.
3. **Combine:** Merge the two sorted halves into a single sorted array.

---

## 🔹 Why Merge Sort?

* **Time Complexity:**

  * Best Case: `O(n log n)`
  * Average Case: `O(n log n)`
  * Worst Case: `O(n log n)`
* **Space Complexity:** `O(n)` (requires extra memory for merging).
* **Stable sort** (preserves the order of equal elements).
* **Efficient for large datasets**, unlike Selection or Bubble Sort.

---

## 🔹 Merge Sort Algorithm

1. If the array has **0 or 1 element**, it is already sorted.
2. Otherwise:

   * Divide the array into two halves.
   * Recursively apply merge sort on both halves.
   * Merge the two sorted halves together.

---

## 🔹 Python Code for Merge Sort

```python"""
def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point
        mid = len(arr) // 2

        # Divide the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two halves
        i = j = k = 0

        # Compare elements from both halves and merge
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining elements of left_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy remaining elements of right_half, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)
"""```

---

## 🔹 Example Walkthrough

Take the array:

```
[38, 27, 43, 3, 9, 82, 10]
```

1. **Divide Step:**

   * Split into `[38, 27, 43]` and `[3, 9, 82, 10]`.
   * Keep splitting until single elements remain.

2. **Sorting Single Elements (Base Case):**

   * `[38] [27] [43] [3] [9] [82] [10]`

3. **Merge Step:**

   * Merge `[38]` and `[27]` → `[27, 38]`
   * Merge `[27, 38]` and `[43]` → `[27, 38, 43]`
   * Merge `[3]` and `[9]` → `[3, 9]`
   * Merge `[3, 9]` and `[82]` → `[3, 9, 82]`
   * Merge `[3, 9, 82]` and `[10]` → `[3, 9, 10, 82]`

4. **Final Merge:**

   * Merge `[27, 38, 43]` and `[3, 9, 10, 82]` → `[3, 9, 10, 27, 38, 43, 82]`

---

## 🔹 Output

```
Original array: [38, 27, 43, 3, 9, 82, 10]
Sorted array: [3, 9, 10, 27, 38, 43, 82]
```

---

## 🔹 Summary

* Merge Sort uses **divide and conquer** to sort arrays.
* Runs in `O(n log n)` time for all cases.
* Requires `O(n)` extra space.
* It is a **stable sort**, making it useful in scenarios where the relative order of equal elements matters.
* Works well for **large datasets** and **linked lists**.

---

"""