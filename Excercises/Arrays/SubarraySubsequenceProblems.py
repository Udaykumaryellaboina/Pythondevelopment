

# ✅ Subarray / Subsequence Problems (21–28)

## 21. Maximum Subarray Sum (Kadane’s Algorithm)

# Without inbuilt
def max_subarray_sum(arr):
    max_sum = arr[0]
    curr_sum = arr[0]
    for i in range(1, len(arr)):
        curr_sum = arr[i] if arr[i] > curr_sum + arr[i] else curr_sum + arr[i]
        max_sum = curr_sum if curr_sum > max_sum else max_sum
    return max_sum

# With inbuilt
def max_subarray_sum_inbuilt(arr):
    max_sum = arr[0]
    curr_sum = arr[0]
    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum

print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))        # 6
print(max_subarray_sum_inbuilt([-2,1,-3,4,-1,2,1,-5,4])) # 6


## 22. Subarray with Given Sum = `k`

# Without inbuilt (brute force O(n^2))
def subarray_sum(arr, k):
    n = len(arr)
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            if s == k:
                return arr[i:j+1]
    return []

# With inbuilt (prefix sum + dict)
def subarray_sum_inbuilt(arr, k):
    prefix_sum, seen = 0, {0: -1}
    for i, num in enumerate(arr):
        prefix_sum += num
        if prefix_sum - k in seen:
            return arr[seen[prefix_sum-k]+1:i+1]
        seen[prefix_sum] = i
    return []

print(subarray_sum([1,2,3,7,5], 12))         # [2,3,7]
print(subarray_sum_inbuilt([1,2,3,7,5], 12)) # [2,3,7]


## 23. Longest Subarray with Sum = `k`

# Without inbuilt
def longest_subarray_sum(arr, k):
    n = len(arr)
    max_len = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            if s == k and (j-i+1) > max_len:
                max_len = j-i+1
    return max_len

# With inbuilt (prefix sum + hashmap)
def longest_subarray_sum_inbuilt(arr, k):
    prefix_sum, seen, max_len = 0, {}, 0
    for i, num in enumerate(arr):
        prefix_sum += num
        if prefix_sum == k:
            max_len = i+1
        if prefix_sum-k in seen:
            max_len = max(max_len, i - seen[prefix_sum-k])
        if prefix_sum not in seen:
            seen[prefix_sum] = i
    return max_len

print(longest_subarray_sum([1,2,3,1,1,1,1,2], 3))         # 2
print(longest_subarray_sum_inbuilt([1,2,3,1,1,1,1,2], 3)) # 2


## 24. Longest Subarray with Equal 0s and 1s

# Without inbuilt (brute force O(n^2))
def longest_equal_01(arr):
    n = len(arr)
    max_len = 0
    for i in range(n):
        zeros, ones = 0, 0
        for j in range(i, n):
            if arr[j] == 0:
                zeros += 1
            else:
                ones += 1
            if zeros == ones and (j-i+1) > max_len:
                max_len = j-i+1
    return max_len

# With inbuilt (prefix sum + hashmap)
def longest_equal_01_inbuilt(arr):
    s, seen, max_len = 0, {0: -1}, 0
    for i, num in enumerate(arr):
        s += 1 if num == 1 else -1
        if s in seen:
            max_len = max(max_len, i - seen[s])
        else:
            seen[s] = i
    return max_len

print(longest_equal_01([0,1,0,1,1,0,0]))        # 6
print(longest_equal_01_inbuilt([0,1,0,1,1,0,0])) # 6


## 25. Maximum Product Subarray

# Without inbuilt
def max_product_subarray(arr):
    max_prod = min_prod = result = arr[0]
    for i in range(1, len(arr)):
        num = arr[i]
        temp_max = max_prod
        max_prod = num if num > max(num, min_prod*num) else max(num, min_prod*num)
        min_prod = num if num < min(num, temp_max*num) else min(num, temp_max*num)
        result = result if result > max_prod else max_prod
    return result

# With inbuilt
def max_product_subarray_inbuilt(arr):
    max_prod = min_prod = result = arr[0]
    for num in arr[1:]:
        choices = (num, max_prod*num, min_prod*num)
        max_prod = max(choices)
        min_prod = min(choices)
        result = max(result, max_prod)
    return result

print(max_product_subarray([2,3,-2,4]))         # 6
print(max_product_subarray_inbuilt([2,3,-2,4])) # 6


## 26. Count Subarrays with Sum = `k`

# Without inbuilt (brute force O(n^2))
def count_subarrays_sum(arr, k):
    n = len(arr)
    count = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            if s == k:
                count += 1
    return count

# With inbuilt (prefix sum + hashmap)
def count_subarrays_sum_inbuilt(arr, k):
    prefix_sum, seen, count = 0, {0:1}, 0
    for num in arr:
        prefix_sum += num
        count += seen.get(prefix_sum-k, 0)
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
    return count

print(count_subarrays_sum([1,2,3], 3))         # 2 ([1,2], [3])
print(count_subarrays_sum_inbuilt([1,2,3], 3)) # 2


## 27. Minimum Length Subarray with Sum ≥ `k`

# Without inbuilt (brute force O(n^2))
def min_len_subarray(arr, k):
    n = len(arr)
    min_len = n+1
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            if s >= k and (j-i+1) < min_len:
                min_len = j-i+1
                break
    return 0 if min_len == n+1 else min_len

# With inbuilt (sliding window O(n))
def min_len_subarray_inbuilt(arr, k):
    left, s, min_len = 0, 0, float('inf')
    for right in range(len(arr)):
        s += arr[right]
        while s >= k:
            min_len = min(min_len, right-left+1)
            s -= arr[left]
            left += 1
    return 0 if min_len == float('inf') else min_len

print(min_len_subarray([2,3,1,2,4,3], 7))         # 2 ([4,3])
print(min_len_subarray_inbuilt([2,3,1,2,4,3], 7)) # 2


## 28. Longest Increasing Subarray

# Without inbuilt
def longest_increasing_subarray(arr):
    max_len = curr_len = 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            curr_len += 1
            if curr_len > max_len:
                max_len = curr_len
        else:
            curr_len = 1
    return max_len

# With inbuilt
def longest_increasing_subarray_inbuilt(arr):
    from itertools import groupby
    max_len, curr_len = 1, 1
    for i in range(1, len(arr)):
        curr_len = curr_len+1 if arr[i] > arr[i-1] else 1
        max_len = max(max_len, curr_len)
    return max_len

print(longest_increasing_subarray([1,2,2,3,4,1,2,3]))         # 3
print(longest_increasing_subarray_inbuilt([1,2,2,3,4,1,2,3])) # 3
