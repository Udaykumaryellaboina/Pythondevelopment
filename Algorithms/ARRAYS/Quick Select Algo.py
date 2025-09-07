"""Perfect 👍
Let’s now go step by step into **Quick Select Algorithm** — I’ll 
explain it in **layman’s terms**, with **examples + Python code** just 
like we did for Kadane, Floyd, and KMP.

---

# 🔹 Problem Statement

We want to find the **k-th smallest (or largest) element** in an unsorted array.

👉 Example:

```
arr = [7, 10, 4, 3, 20, 15]
k = 3
```

Answer → `7` (the 3rd smallest element).

---

# 🔹 The Naive Way

* Sort the array → pick the `k`th element.
* Sorting takes `O(n log n)`.

But we don’t need the full sort! 🚀
We only care about the `k`th element.
That’s where **Quick Select** comes in.

---

# 🔹 Why Quick Select?

Quick Select is like **Quick Sort**, but instead of sorting everything, it only works on the side where the `k`th element lies.
👉 This makes it faster:

* **Average case:** `O(n)`
* **Worst case:** `O(n²)` (rare, if pivots are chosen poorly).

---

# 🔹 Layman’s Terms Explanation

Imagine you’re in a cooking competition with **20 dishes**.
The judge only wants the **5th tastiest dish**.

Instead of ranking all 20 dishes:

1. You pick one dish as a **pivot**.
2. Split dishes into:

   * tastier than pivot (right side)
   * less tasty than pivot (left side)
3. Now:

   * If pivot happens to be the 5th tastiest → done ✅
   * If pivot rank > 5 → only look in the **left half**
   * If pivot rank < 5 → only look in the **right half**

Repeat until you find the dish → no need to sort everything.

---

# 🔹 Step by Step Example

Find 3rd smallest in:

```
arr = [7, 10, 4, 3, 20, 15], k = 3
```

1. Pick pivot = `15`
   Partition → `[7, 10, 4, 3] [15] [20]`
   Pivot position = 5 → too far right
   Look left `[7, 10, 4, 3]`

2. Pick pivot = `4`
   Partition → `[3] [4] [7, 10]`
   Pivot position = 2

   Since we want 3rd smallest → look in right side `[7, 10]`

3. Pick pivot = `7`
   Partition → `[] [7] [10]`
   Pivot position = 3 ✅ Done

Answer = `7`.

---

# 🔹 Python Code with Explanation

```python"""
import random

def partition(arr, left, right):
    """Partition the array using Lomuto's scheme."""
    pivot = arr[right]
    i = left

    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]
    return i  # final position of pivot


def quickselect(arr, left, right, k):
    """Quick Select algorithm to find k-th smallest element."""
    if left <= right:
        # Choose random pivot for better performance
        pivot_index = random.randint(left, right)
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

        pi = partition(arr, left, right)

        # If pivot is at (k-1) → found the k-th smallest
        if pi == k - 1:
            return arr[pi]
        elif pi > k - 1:
            return quickselect(arr, left, pi - 1, k)
        else:
            return quickselect(arr, pi + 1, right, k)


# Example usage
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(f"{k}rd smallest element is:", quickselect(arr, 0, len(arr) - 1, k))
"""```

---

# 🔹 Output

```
3rd smallest element is: 7
```

---

# 🔹 Time & Space Complexity

* **Average time:** `O(n)`
* **Worst time:** `O(n²)` (rare, happens if pivots are always bad)
* **Space:** `O(1)` (in-place, ignoring recursion stack).

---

# 🔹 Real-Life Analogy

Imagine you’re finding the **5th fastest runner** in a race:

* You don’t need to rank everyone.
* You pick a random runner as pivot → divide runners into faster/slower.
* Depending on where pivot lands, you only focus on one side.
* Repeat until you find exactly the `k`th runner.

That’s Quick Select 🎯

---

👉 Do you want me to also extend this to explain how **Quick Select can be used to find the k-th largest element** (instead of smallest) with just a small tweak?
"""