


"""# Bubble Sort – Explanation and Code

## 🔹 What is Bubble Sort?

Bubble Sort is the **simplest comparison-based sorting algorithm**.

It repeatedly **swaps adjacent elements** if they are in the wrong order. 
After each pass, the largest element "bubbles up" to its correct position at the end of the array.

---

## 🔹 How Bubble Sort Works (Step by Step)

1. Start from the beginning of the array.
2. Compare the first two adjacent elements.

   * If the first is greater than the second → swap them.
3. Move to the next pair, and repeat until the end of the array.
4. After the first pass, the **largest element is at the end**.
5. Repeat the process for the remaining elements (ignoring the last sorted ones).
6. Continue until no swaps are needed → array is sorted.

---

## 🔹 Why Bubble Sort?

* **Time Complexity:**

  * Best Case: `O(n)` (if array already sorted, with optimization).
  * Average Case: `O(n²)`
  * Worst Case: `O(n²)`
* **Space Complexity:** `O(1)` (in-place sorting).
* **Stable sort** (preserves the order of equal elements).
* **Easy to understand**, but very inefficient for large datasets.

---

## 🔹 Bubble Sort Algorithm

1. Loop `i` from `0` to `n-1`.
2. For each pass, loop `j` from `0` to `n-i-1`.
3. Compare adjacent elements `arr[j]` and `arr[j+1]`.
4. Swap if they are in the wrong order.
5. Stop early if no swaps happen in a pass (optimization).

---

## 🔹 Python Code for Bubble Sort

```python"""
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False  # Optimization: check if any swap happens
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps happened → array is already sorted
        if not swapped:
            break


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
bubble_sort(arr)
print("Sorted array:", arr)
"""```

---

## 🔹 Example Walkthrough

Take the array:

```
[64, 34, 25, 12, 22, 11, 90]
```

1. **Pass 1:**
   After comparing/swapping → `[34, 25, 12, 22, 11, 64, 90]`
   (largest `90` is bubbled to the end).

2. **Pass 2:**
   → `[25, 12, 22, 11, 34, 64, 90]`

3. **Pass 3:**
   → `[12, 22, 11, 25, 34, 64, 90]`

4. **Pass 4:**
   → `[12, 11, 22, 25, 34, 64, 90]`

5. **Pass 5:**
   → `[11, 12, 22, 25, 34, 64, 90]`

Array is now sorted.

---

## 🔹 Output

```
Original array: [64, 34, 25, 12, 22, 11, 90]
Sorted array: [11, 12, 22, 25, 34, 64, 90]
```

---

## 🔹 Summary

* Bubble Sort works by **repeatedly swapping adjacent elements** until the array is sorted.
* It is **stable** and **in-place**, but very inefficient (`O(n²)`).
* Useful only for **small datasets or teaching purposes**.
* Rarely used in practice compared to **Merge Sort, Quick Sort, or Heap Sort**.

---

"""