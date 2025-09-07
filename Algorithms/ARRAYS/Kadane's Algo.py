"""Got it 👍
Let’s go step by step — I’ll explain **Kadane’s Algorithm** like I’m teaching from scratch, in **layman’s terms**, and then show you **Python code with explanation**.

---

# 🔹 Problem Statement

We want to solve:

👉 **Find the maximum sum of a contiguous subarray in a given array.**

For example:

```
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

The maximum sum subarray is `[4, -1, 2, 1]` and its sum is `6`.

---

# 🔹 Why Kadane’s Algorithm?

* The brute force way is to check all possible subarrays → this takes **O(n²)** or **O(n³)** time.
* Kadane’s Algorithm gives a smart way to do it in **O(n)** (linear time).

---

# 🔹 Layman’s Terms Explanation

Think of it like walking through the array and keeping a "running sum":

1. Start with the first element.
2. Keep adding the next elements to your running sum.
3. If at any point the running sum becomes **negative**, drop it and start fresh from the next element.

   * Because a negative running sum will only **drag down** future sums.
4. While doing this, keep track of the **maximum sum you’ve seen so far**.

---

# 🔹 Step by Step Example

Array: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`

* Start:
  `max_so_far = -2`, `current_sum = -2`

* Next (1):
  `current_sum = max(1, -2+1) = 1`
  `max_so_far = max(-2, 1) = 1`

* Next (-3):
  `current_sum = max(-3, 1+(-3)) = -2`
  `max_so_far = 1`

* Next (4):
  `current_sum = max(4, -2+4) = 4`
  `max_so_far = 4`

* Next (-1):
  `current_sum = max(-1, 4+(-1)) = 3`
  `max_so_far = 4`

* Next (2):
  `current_sum = max(2, 3+2) = 5`
  `max_so_far = 5`

* Next (1):
  `current_sum = max(1, 5+1) = 6`
  `max_so_far = 6`

* Next (-5):
  `current_sum = max(-5, 6+(-5)) = 1`
  `max_so_far = 6`

* Next (4):
  `current_sum = max(4, 1+4) = 5`
  `max_so_far = 6`

✅ Answer = `6`

---

# 🔹 Python Code with Explanation

```python"""
def kadane(arr):
    # Step 1: Initialize variables
    max_so_far = arr[0]       # best sum found so far
    current_sum = arr[0]      # current running sum

    # Step 2: Loop through the array starting from second element
    for i in range(1, len(arr)):
        num = arr[i]

        # Either take the current number alone, or add it to current_sum
        current_sum = max(num, current_sum + num)

        # Update max_so_far if we found a bigger sum
        max_so_far = max(max_so_far, current_sum)

    return max_so_far


# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum subarray sum is:", kadane(arr))
"""```

---

# 🔹 Output

```
Maximum subarray sum is: 6
```

---

# 🔹 Time & Space Complexity

* **Time:** `O(n)` → Only one loop through the array.
* **Space:** `O(1)` → Only a few variables used.

---

# 🔹 Real-Life Analogy

Imagine you are tracking your **daily profits**:

* If your running profit becomes negative, it’s better to **reset and start fresh** from the next day.
* Keep note of the **best streak** of profit you’ve ever had.

That’s **Kadane’s Algorithm** 😃"""