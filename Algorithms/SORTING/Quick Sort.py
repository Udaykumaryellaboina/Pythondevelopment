

"""
# Quick Sort – Explanation and Code

---

## 🔹 What is Quick Sort?

Quick Sort is a **divide and conquer sorting algorithm** that works by selecting a **pivot element**, partitioning the array around the pivot, and then recursively sorting the sub-arrays.

It is one of the fastest sorting algorithms in practice and is widely used in real-world applications.

---

## 🔹 How Quick Sort Works (Step by Step)

1. **Choose a Pivot:** Pick an element as the pivot (commonly the last element, but other strategies exist).
2. **Partition:** Rearrange elements so that:

   * Elements **smaller than the pivot** go to the left.
   * Elements **greater than the pivot** go to the right.
3. **Recursively Apply:** Apply Quick Sort on the left and right sub-arrays.
4. **Combine:** Since sorting is done in place, the array becomes sorted when recursion ends.

---

## 🔹 Why Quick Sort?

* **Time Complexity:**

  * Best Case: `O(n log n)` (balanced partitions).
  * Average Case: `O(n log n)`
  * Worst Case: `O(n²)` (if pivot choice is poor, e.g., sorted array with last element as pivot).
* **Space Complexity:** `O(log n)` (due to recursion stack).
* **Not stable** (relative order of equal elements may change).
* **Very efficient in practice** because of good cache performance and fewer comparisons.

---

## 🔹 Quick Sort Algorithm

1. Pick a pivot element.
2. Partition the array into two sub-arrays: elements smaller than pivot, elements larger than pivot.
3. Recursively apply Quick Sort on the sub-arrays.
4. Combine results (in-place).

---

## 🔹 Python Code for Quick Sort

```python"""
def partition(arr, low, high):
    # Choose the last element as pivot
    pivot = arr[high]
    i = low - 1  # index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap if element <= pivot

    # Place pivot at the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        # Partition index
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Example usage
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
"""```

---

## 🔹 Example Walkthrough

Take the array:

```
[10, 7, 8, 9, 1, 5]
```

1. **First Partition:**

   * Pivot = `5`
   * Rearranged → `[1, 5, 8, 9, 10, 7]`
   * Pivot `5` is placed in correct position (index `1`).

2. **Left Sub-array:** `[1]` → already sorted.

3. **Right Sub-array:** `[8, 9, 10, 7]`

   * Pivot = `7`
   * Rearranged → `[7, 9, 10, 8]`
   * Pivot `7` at correct position.

4. Continue partitioning until all sub-arrays are of size 1.

Final sorted array → `[1, 5, 7, 8, 9, 10]`.

---

## 🔹 Output

```
Original array: [10, 7, 8, 9, 1, 5]
Sorted array: [1, 5, 7, 8, 9, 10]
```

---

## 🔹 Summary

* Quick Sort uses **divide and conquer** with partitioning around a pivot.
* Average case runs in `O(n log n)`, but worst case is `O(n²)`.
* Performs better than Merge Sort in practice (due to lower memory overhead).
* **In-place** but **not stable**.
* One of the **most widely used sorting algorithms** in libraries and systems.

---


"""