

# ✅ Array Interview Problems in Python (Both Ways)


## 1. Find the largest element

# 🔹 Without inbuilt
def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

# 🔹 With inbuilt
def find_largest_inbuilt(arr):
    return max(arr)

print(find_largest([5, 9, 2, 11, 7]))       # 11
print(find_largest_inbuilt([5, 9, 2, 11, 7]))  # 11


## 2. Find the smallest element

# Without inbuilt
def find_smallest(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

# With inbuilt
def find_smallest_inbuilt(arr):
    return min(arr)

print(find_smallest([5, 9, 2, 11, 7]))       # 2
print(find_smallest_inbuilt([5, 9, 2, 11, 7])) # 2


## 3. Second largest / second smallest

# Without inbuilt
def second_largest(arr):
    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second

def second_smallest(arr):
    smallest = second = float('inf')
    for num in arr:
        if num < smallest:
            second = smallest
            smallest = num
        elif num < second and num != smallest:
            second = num
    return second

# With inbuilt
def second_largest_inbuilt(arr):
    return sorted(set(arr))[-2]

def second_smallest_inbuilt(arr):
    return sorted(set(arr))[1]

print(second_largest([5, 9, 2, 11, 7]))       # 9
print(second_smallest([5, 9, 2, 11, 7]))      # 5
print(second_largest_inbuilt([5, 9, 2, 11, 7]))  # 9
print(second_smallest_inbuilt([5, 9, 2, 11, 7])) # 5


## 4. Reverse an array

# Without inbuilt
def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return arr

# With inbuilt
def reverse_array_inbuilt(arr):
    return arr[::-1]

print(reverse_array([1,2,3,4,5]))        # [5,4,3,2,1]
print(reverse_array_inbuilt([1,2,3,4,5])) # [5,4,3,2,1]


## 5. Rotate array left/right by `k`

# Without inbuilt
def rotate_left(arr, k):
    n = len(arr)
    k %= n
    rotated = []
    for i in range(n):
        rotated.append(arr[(i+k) % n])
    return rotated

def rotate_right(arr, k):
    n = len(arr)
    k %= n
    rotated = []
    for i in range(n):
        rotated.append(arr[(i-k) % n])
    return rotated

# With inbuilt
def rotate_left_inbuilt(arr, k):
    k %= len(arr)
    return arr[k:] + arr[:k]

def rotate_right_inbuilt(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

print(rotate_left([1,2,3,4,5], 2))         # [3,4,5,1,2]
print(rotate_right([1,2,3,4,5], 2))        # [4,5,1,2,3]
print(rotate_left_inbuilt([1,2,3,4,5], 2)) # [3,4,5,1,2]
print(rotate_right_inbuilt([1,2,3,4,5], 2))# [4,5,1,2,3]


## 6. Sum of elements

# Without inbuilt
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

# With inbuilt
def sum_array_inbuilt(arr):
    return sum(arr)

print(sum_array([1,2,3,4,5]))       # 15
print(sum_array_inbuilt([1,2,3,4,5])) # 15


## 7. Average of elements

# Without inbuilt
def average_array(arr):
    total = 0
    count = 0
    for num in arr:
        total += num
        count += 1
    return total / count

# With inbuilt
def average_array_inbuilt(arr):
    return sum(arr) / len(arr)

print(average_array([1,2,3,4,5]))       # 3.0
print(average_array_inbuilt([1,2,3,4,5])) # 3.0


## 8. Count even and odd numbers

# Without inbuilt
def count_even_odd(arr):
    even = odd = 0
    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

# With inbuilt
def count_even_odd_inbuilt(arr):
    even = len([x for x in arr if x % 2 == 0])
    odd = len(arr) - even
    return even, odd

print(count_even_odd([1,2,3,4,5,6]))        # (3,3)
print(count_even_odd_inbuilt([1,2,3,4,5,6])) # (3,3)


## 9. Check if array is sorted

# Without inbuilt
def is_sorted(arr):
    ascending = descending = True
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            ascending = False
        if arr[i] > arr[i-1]:
            descending = False
    if ascending: return "Ascending"
    if descending: return "Descending"
    return "Not Sorted"

# With inbuilt
def is_sorted_inbuilt(arr):
    if arr == sorted(arr):
        return "Ascending"
    elif arr == sorted(arr, reverse=True):
        return "Descending"
    else:
        return "Not Sorted"

print(is_sorted([1,2,3,4]))         # Ascending
print(is_sorted([9,7,5,2]))         # Descending
print(is_sorted([3,1,4,2]))         # Not Sorted
print(is_sorted_inbuilt([1,2,3,4])) # Ascending

## 10. Merge two sorted arrays

# Without inbuilt (two-pointer technique)
def merge_sorted(arr1, arr2):
    i = j = 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    return merged

# With inbuilt
def merge_sorted_inbuilt(arr1, arr2):
    return sorted(arr1 + arr2)

print(merge_sorted([1,3,5], [2,4,6]))        # [1,2,3,4,5,6]
print(merge_sorted_inbuilt([1,3,5], [2,4,6])) # [1,2,3,4,5,6]
