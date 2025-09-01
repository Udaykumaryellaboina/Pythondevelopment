
"""
## 🔹 What is Heap Sort?

Heap Sort is a **comparison-based sorting algorithm** that uses a 
**Binary Heap** (usually a Max Heap) to sort elements.

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

Perfect 👌 Let’s **break the code line by line** so you understand it like a story.

We’ll go in **two parts**:

1. `heapify` function (the heart of Heap Sort).
2. `heap_sort` function (uses heapify to actually sort).

---

## 🔹 1. The `heapify` Function

```python
def heapify(arr, n, i):
    largest = i          # Assume the current root is the largest
    left = 2 * i + 1     # Index of left child
    right = 2 * i + 2    # Index of right child
```

👉 This calculates the **position of children** in the binary heap (stored as an array).

* If `i = 0` (root), left = 1, right = 2.
* If `i = 1`, left = 3, right = 4, etc.

---

```python
    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
```

👉 Checks if left child exists (`left < n`) and is greater than current `largest`.
If yes → update `largest`.

---

```python
    # If right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
```

👉 Same for the right child.
So now, `largest` points to the **biggest value among root, left child, right child**.

---

```python
    # If root is not largest, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)  # Recursively heapify the affected subtree
```

👉 If root was not the largest, swap root with the largest child.
👉 Then call `heapify` recursively to fix the subtree where the swap happened.

✅ This ensures that the heap property (parent ≥ children) holds.

---

## 🔹 2. The `heap_sort` Function

```python
def heap_sort(arr):
    n = len(arr)
```

👉 Store the array size.

---

### Step 1: Build a Max Heap

```python
    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):   # Start from last non-leaf node
        heapify(arr, n, i)
```

👉 Why `n // 2 - 1`?

* All nodes from `n//2` to `n-1` are **leaf nodes**.
* Leaf nodes already satisfy heap property (no children).
* So, we only heapify **non-leaf nodes** (going backwards).

✅ After this loop, the entire array is a **Max Heap**.

---

### Step 2: Extract Elements from Heap

```python
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]   # Swap root with last element
        heapify(arr, i, 0)                # Heapify reduced heap
```

👉 What happens here?

* `arr[0]` is the **largest element** (root of max heap).
* Swap it with the **last element** in the heap.
* Now reduce heap size by 1 (`i` is the new heap size).
* Call `heapify` again to restore max heap property.

✅ This step keeps moving the largest element to the end until the array is sorted.

---

## 🔹 Example Walkthrough

Let’s take:

```
arr = [12, 11, 13, 5, 6, 7]
```

1. **Build max heap** → `[13, 11, 12, 5, 6, 7]`
   (largest element `13` moved to root).

2. **Extract 1st max (13):**
   Swap root with last → `[7, 11, 12, 5, 6, 13]`
   Heapify again → `[12, 11, 7, 5, 6, 13]`.

3. **Extract 2nd max (12):**
   Swap → `[6, 11, 7, 5, 12, 13]`
   Heapify → `[11, 6, 7, 5, 12, 13]`.

4. Keep going...
   Final sorted array → `[5, 6, 7, 11, 12, 13]`.

---

## 🔹 Output Recap

```
Original array: [12, 11, 13, 5, 6, 7]
Sorted array: [5, 6, 7, 11, 12, 13]
```

---


"""