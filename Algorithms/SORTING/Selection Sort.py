"""
---

## 🔹 What is Selection Sort?

Selection Sort is one of the simplest **comparison-based sorting algorithms**.

It works by **repeatedly finding the smallest element** from the 
unsorted part of the array and moving it to the beginning.

---

## 🔹 How Selection Sort Works (Step by Step)

1. Start with the first element (at index `0`).
2. Find the **minimum element** from the unsorted part of the array.
3. Swap the minimum element with the element at the beginning of the unsorted part.
4. Move the boundary of the sorted part forward by one.
5. Repeat until the whole array is sorted.

---

## 🔹 Why Selection Sort?

* **Time Complexity:**

  * Best Case: `O(n²)`
  * Average Case: `O(n²)`
  * Worst Case: `O(n²)`
* **Space Complexity:** `O(1)` (in-place sorting).
* **Not stable** (equal elements may lose their relative order).
* **Very easy to understand**, but inefficient for large datasets 
compared to Heap Sort, Merge Sort, or Quick Sort.

---

## 🔹 Selection Sort Algorithm

1. Loop `i` from `0` to `n-1`.
2. Assume `i` is the index of the minimum element.
3. Compare with every other element in the unsorted part.
4. Update index of the minimum if a smaller element is found.
5. Swap the found minimum with element at index `i`.

---

## 🔹 Python Code for Selection Sort"""


def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all elements
    for i in range(n):
        # Assume the minimum is the first element in the unsorted part
        min_index = i
        
        # Find the index of the minimum element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Example usage
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)
selection_sort(arr)
print("Sorted array:", arr)
"""```

---

## 🔹 Example Walkthrough

Take the array:

```
[64, 25, 12, 22, 11]
```

1. **Pass 1:**

   * Minimum element = `11`
   * Swap with first element → `[11, 25, 12, 22, 64]`

2. **Pass 2:**

   * Minimum element = `12`
   * Swap with second element → `[11, 12, 25, 22, 64]`

3. **Pass 3:**

   * Minimum element = `22`
   * Swap with third element → `[11, 12, 22, 25, 64]`

4. **Pass 4:**

   * Minimum element = `25`
   * Swap with fourth element → `[11, 12, 22, 25, 64]`

5. **Pass 5:**

   * Last element already in place → `[11, 12, 22, 25, 64]`

---

## 🔹 Output

```
Original array: [64, 25, 12, 22, 11]
Sorted array: [11, 12, 22, 25, 64]
```

---

## 🔹 Summary

* Selection Sort repeatedly finds the minimum element and puts it in the correct position.
* It has **O(n²)** time complexity regardless of input.
* It is **in-place** but **not stable**.
* Useful for **small datasets** or when simplicity is more important than performance.

---

"""