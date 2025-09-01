
"""
## 🔹 What is Heap Sort?

Heap Sort is a **comparison-based sorting algorithm** that uses a **Binary Heap** (usually a Max Heap) to sort elements.

It works in **two main steps**:

1. **Build a Max Heap** from the array.

   * A Max Heap is a complete binary tree where each node is greater than or equal to its children.
   * This ensures the **largest element is always at the root** (index `0`).

2. **Extract elements from the heap one by one**:

   * Swap the root (largest element) with the last element in the heap.
   * Reduce the heap size by 1.
   * Heapify the root again to restore the heap property.
   * Repeat until the array is sorted.

---

## 🔹 Why Heap Sort?

* **Time Complexity:** `O(n log n)` (in all cases: best, average, worst).
* **Space Complexity:** `O(1)` (in-place sorting).
* **Not stable** (doesn’t preserve order of equal elements).

---

## 🔹 How Heapify Works (Core Step)

* Heapify ensures the **subtree rooted at index `i`** satisfies the heap property.
* Steps:

  1. Assume index `i` has children `left = 2*i+1`, `right = 2*i+2`.
  2. Find the largest among `i`, `left`, and `right`.
  3. If the largest is not `i`, swap `i` with the largest and recursively call `heapify`.

---

## 🔹 Algorithm (Step by Step)

1. **Build a max heap** from the array (`heapify` called for all non-leaf nodes).
2. Swap the root with the last element and reduce heap size.
3. Call `heapify` on the reduced heap.
4. Repeat until sorted.

---

## 🔹 Python Code for Heap Sort

```python"""
def heapify(arr, n, i):
    """Ensure the subtree rooted at index i is a max heap."""
    largest = i          # Assume root is largest
    left = 2 * i + 1     # left child
    right = 2 * i + 2    # right child

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not largest, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)  # Recursive heapify


def heap_sort(arr):
    n = len(arr)

    # Step 1: Build a max heap
    for i in range(n // 2 - 1, -1, -1):   # Start from last non-leaf node
        heapify(arr, n, i)

    # Step 2: Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]   # Swap root with last element
        heapify(arr, i, 0)                # Heapify reduced heap


# Example usage
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
heap_sort(arr)
print("Sorted array:", arr)
""""
## 🔹 Output

```
Original array: [12, 11, 13, 5, 6, 7]
Sorted array: [5, 6, 7, 11, 12, 13]
```

---

✅ So Heap Sort is just:

1. Build Max Heap
2. Repeatedly swap root with last element
3. Heapify again

"""