

# Counting Sort – Explanation and Code


"""## 🔹 What is Counting Sort?

Counting Sort is a **non-comparison-based sorting algorithm**.

Instead of comparing elements (like Quick Sort or Merge Sort), it works by **counting the number of occurrences** of each element in the input.

It is mainly useful when:

* The input elements are **integers**.
* The range of elements (`max - min`) is **not significantly larger than the number of elements**.

---

## 🔹 How Counting Sort Works (Step by Step)

1. **Find the maximum element** in the array (let’s call it `k`).
2. **Create a count array** of size `k+1`, initialized with zeros.
3. **Count each element’s frequency** by iterating through the input array.
4. **Update count array** to store cumulative counts (this tells us positions of elements in the sorted array).
5. **Build the output array** by placing elements in their correct positions using the count array.
6. Copy the output array back to the original array.

---

## 🔹 Why Counting Sort?

* **Time Complexity:**

  * Best Case: `O(n + k)`
  * Average Case: `O(n + k)`
  * Worst Case: `O(n + k)`
* **Space Complexity:** `O(n + k)` (extra space needed for count and output arrays).
* **Stable sort** (if implemented properly).
* **Efficient for small ranges**, but **not suitable for large ranges** (e.g., sorting numbers up to billions).

---

## 🔹 Counting Sort Algorithm

1. Find the maximum element in the array.
2. Initialize a count array of that size.
3. Count occurrences of each element.
4. Compute cumulative sums to determine positions.
5. Build the output array.
6. Copy it back to the original.

---

## 🔹 Python Code for Counting Sort

```python"""
def counting_sort(arr):
    # Step 1: Find the maximum element
    max_val = max(arr)
    
    # Step 2: Initialize count array
    count = [0] * (max_val + 1)
    
    # Step 3: Count the occurrences of each element
    for num in arr:
        count[num] += 1
    
    # Step 4: Update count[i] to store cumulative sum
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Step 5: Build the output array (stable)
    output = [0] * len(arr)
    for num in reversed(arr):  # reversed to maintain stability
        output[count[num] - 1] = num
        count[num] -= 1
    
    # Step 6: Copy sorted elements back into original array
    for i in range(len(arr)):
        arr[i] = output[i]


# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
print("Original array:", arr)
counting_sort(arr)
print("Sorted array:", arr)
"""```

---

## 🔹 Example Walkthrough

Take the array:

```
[4, 2, 2, 8, 3, 3, 1]
```

1. **Find max element:** `8`
   → Create count array of size `9` → `[0,0,0,0,0,0,0,0,0]`

2. **Count occurrences:**
   After counting → `[0,1,2,2,1,0,0,0,1]`
   (meaning: one `1`, two `2`s, two `3`s, one `4`, one `8`)

3. **Cumulative sum:**
   → `[0,1,3,5,6,6,6,6,7]`
   (now each index tells us the final position of that number).

4. **Build output (placing elements in correct order):**
   → `[1, 2, 2, 3, 3, 4, 8]`

---

## 🔹 Output

```
Original array: [4, 2, 2, 8, 3, 3, 1]
Sorted array: [1, 2, 2, 3, 3, 4, 8]
```

---

## 🔹 Summary

* Counting Sort is a **non-comparison sorting algorithm**.
* Runs in `O(n + k)` time, where `k` is the range of input values.
* Requires extra memory (`O(n + k)`), so it is **not memory efficient for large ranges**.
* **Stable sort**, which makes it suitable for sorting objects by multiple keys.
* Best for integers with a **small range** relative to the array size.

---

"""