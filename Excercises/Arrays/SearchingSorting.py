
# ✅ Array Interview Problems (11–20)


## 11. Linear Search

# Without inbuilt
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# With inbuilt
def linear_search_inbuilt(arr, target):
    return arr.index(target) if target in arr else -1

print(linear_search([2, 4, 6, 8], 6))          # 2
print(linear_search_inbuilt([2, 4, 6, 8], 6))  # 2


## 12. Binary Search (Iterative + Recursive)

# Without inbuilt - Iterative
def binary_search_iter(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1

# Without inbuilt - Recursive
def binary_search_rec(arr, target, low, high):
    if low > high:
        return -1
    mid = (low+high)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_rec(arr, target, mid+1, high)
    else:
        return binary_search_rec(arr, target, low, mid-1)

# With inbuilt
import bisect
def binary_search_inbuilt(arr, target):
    idx = bisect.bisect_left(arr, target)
    return idx if idx < len(arr) and arr[idx] == target else -1

print(binary_search_iter([1,3,5,7,9], 7))             # 3
print(binary_search_rec([1,3,5,7,9], 7, 0, 4))        # 3
print(binary_search_inbuilt([1,3,5,7,9], 7))          # 3


## 13. First and Last Occurrence

# Without inbuilt
def first_last_occurrence(arr, target):
    first, last = -1, -1
    for i in range(len(arr)):
        if arr[i] == target:
            if first == -1:
                first = i
            last = i
    return first, last

# With inbuilt
def first_last_inbuilt(arr, target):
    if target not in arr:
        return -1, -1
    return arr.index(target), len(arr) - 1 - arr[::-1].index(target)

print(first_last_occurrence([1,2,3,2,4,2], 2))   # (1,5)
print(first_last_inbuilt([1,2,3,2,4,2], 2))      # (1,5)


## 14. Count Occurrences

# Without inbuilt
def count_occurrence(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

# With inbuilt
def count_occurrence_inbuilt(arr, target):
    return arr.count(target)

print(count_occurrence([1,2,3,2,2,4], 2))          # 3
print(count_occurrence_inbuilt([1,2,3,2,2,4], 2))  # 3


## 15. Missing Number in `1..n`

# Without inbuilt
def missing_number(arr, n):
    expected_sum = n * (n+1) // 2
    actual_sum = 0
    for num in arr:
        actual_sum += num
    return expected_sum - actual_sum

# With inbuilt
def missing_number_inbuilt(arr, n):
    return sum(range(1, n+1)) - sum(arr)

print(missing_number([1,2,4,5], 5))         # 3
print(missing_number_inbuilt([1,2,4,5], 5)) # 3


## 16. Find Duplicate Numbers

# Without inbuilt
def find_duplicates(arr):
    seen, duplicates = [], []
    for num in arr:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        else:
            seen.append(num)
    return duplicates

# With inbuilt (set logic)
def find_duplicates_inbuilt(arr):
    return list({x for x in arr if arr.count(x) > 1})

print(find_duplicates([1,2,3,2,4,1,5,3]))       # [2,1,3]
print(find_duplicates_inbuilt([1,2,3,2,4,1,5,3])) # [1,2,3]


## 17. All Pairs with Sum = k

# Without inbuilt
def find_pairs(arr, k):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                pairs.append((arr[i], arr[j]))
    return pairs

# With inbuilt (set trick)
def find_pairs_inbuilt(arr, k):
    seen, pairs = set(), set()
    for num in arr:
        if k - num in seen:
            pairs.add((min(num, k-num), max(num, k-num)))
        seen.add(num)
    return list(pairs)

print(find_pairs([1,2,3,4,5,6], 7))         # [(1,6),(2,5),(3,4)]
print(find_pairs_inbuilt([1,2,3,4,5,6], 7)) # [(1,6),(2,5),(3,4)]


## 18. Triplets with Sum = k

# Without inbuilt
def find_triplets(arr, k):
    n = len(arr)
    triplets = []
    for i in range(n):
        for j in range(i+1, n):
            for l in range(j+1, n):
                if arr[i] + arr[j] + arr[l] == k:
                    triplets.append((arr[i], arr[j], arr[l]))
    return triplets

# With inbuilt (sorting + two-pointer)
def find_triplets_inbuilt(arr, k):
    arr.sort()
    triplets = []
    n = len(arr)
    for i in range(n-2):
        left, right = i+1, n-1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s == k:
                triplets.append((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1
            elif s < k:
                left += 1
            else:
                right -= 1
    return triplets

print(find_triplets([1,2,3,4,5], 9))        # [(1,3,5),(2,3,4)]
print(find_triplets_inbuilt([1,2,3,4,5], 9))# [(1,3,5),(2,3,4)]


## 19. Bubble / Selection / Insertion Sort

# Bubble Sort (without inbuilt)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# With inbuilt
def sort_inbuilt(arr):
    return sorted(arr)

print(bubble_sort([5,3,1,4,2]))    # [1,2,3,4,5]
print(selection_sort([5,3,1,4,2])) # [1,2,3,4,5]
print(insertion_sort([5,3,1,4,2])) # [1,2,3,4,5]
print(sort_inbuilt([5,3,1,4,2]))   # [1,2,3,4,5]


## 20. Merge Sort / Quick Sort

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i]); i+=1
        else:
            merged.append(right[j]); j+=1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

# With inbuilt
def sort_inbuilt(arr):
    return sorted(arr)

print(merge_sort([5,3,1,4,2])) # [1,2,3,4,5]
print(quick_sort([5,3,1,4,2])) # [1,2,3,4,5]
print(sort_inbuilt([5,3,1,4,2])) # [1,2,3,4,5]

