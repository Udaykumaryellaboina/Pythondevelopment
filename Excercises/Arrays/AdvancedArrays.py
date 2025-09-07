

# ✅ Advanced Array Problems (36–50)


## 36. Majority Element (> n/2 times)

# Without inbuilt (Boyer-Moore Voting Algorithm)
def majority_element(arr):
    count, candidate = 0, None
    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate

# With inbuilt (collections.Counter)
from collections import Counter
def majority_element_inbuilt(arr):
    return Counter(arr).most_common(1)[0][0]

print(majority_element([3,3,4,2,3,3,5]))         # 3
print(majority_element_inbuilt([3,3,4,2,3,3,5])) # 3


## 37. Elements Occurring More Than n/3 Times

# Without inbuilt (Extended Boyer-Moore)
def majority_element_n3(arr):
    cand1, cand2, count1, count2 = None, None, 0, 0
    for num in arr:
        if num == cand1:
            count1 += 1
        elif num == cand2:
            count2 += 1
        elif count1 == 0:
            cand1, count1 = num, 1
        elif count2 == 0:
            cand2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1
    result = []
    for cand in [cand1, cand2]:
        if arr.count(cand) > len(arr)//3:
            result.append(cand)
    return result

# With inbuilt
def majority_element_n3_inbuilt(arr):
    from collections import Counter
    freq = Counter(arr)
    return [num for num, cnt in freq.items() if cnt > len(arr)//3]

print(majority_element_n3([1,2,3,1,2,1,1]))         # [1]
print(majority_element_n3_inbuilt([1,2,3,1,2,1,1])) # [1]


## 38. Equilibrium Index

# Without inbuilt
def equilibrium_index(arr):
    total = 0
    for num in arr:
        total += num
    left_sum = 0
    for i, num in enumerate(arr):
        if left_sum == total - left_sum - num:
            return i
        left_sum += num
    return -1

# With inbuilt
def equilibrium_index_inbuilt(arr):
    total = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        if left_sum == total - left_sum - num:
            return i
        left_sum += num
    return -1

print(equilibrium_index([1,3,5,2,2]))         # 2
print(equilibrium_index_inbuilt([1,3,5,2,2])) # 2


## 39. Trapping Rainwater

# Without inbuilt
def trap_rainwater(arr):
    n = len(arr)
    left_max, right_max = [0]*n, [0]*n
    left_max[0] = arr[0]
    for i in range(1,n):
        left_max[i] = arr[i] if arr[i]>left_max[i-1] else left_max[i-1]
    right_max[-1] = arr[-1]
    for i in range(n-2,-1,-1):
        right_max[i] = arr[i] if arr[i]>right_max[i+1] else right_max[i+1]
    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - arr[i]
    return water

# With inbuilt
def trap_rainwater_inbuilt(arr):
    n = len(arr)
    left_max = [max(arr[:i+1]) for i in range(n)]
    right_max = [max(arr[i:]) for i in range(n)]
    return sum(min(left_max[i], right_max[i]) - arr[i] for i in range(n))

print(trap_rainwater([0,1,0,2,1,0,1,3,2,1,2,1]))         # 6
print(trap_rainwater_inbuilt([0,1,0,2,1,0,1,3,2,1,2,1])) # 6


## 40. Container With Most Water

# Without inbuilt (two pointer)
def max_area(height):
    l, r = 0, len(height)-1
    area = 0
    while l < r:
        area = area if area > min(height[l],height[r])*(r-l) else min(height[l],height[r])*(r-l)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return area

# With inbuilt (same but with max())
def max_area_inbuilt(height):
    l, r, ans = 0, len(height)-1, 0
    while l < r:
        ans = max(ans, min(height[l], height[r])*(r-l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return ans

print(max_area([1,8,6,2,5,4,8,3,7]))         # 49
print(max_area_inbuilt([1,8,6,2,5,4,8,3,7])) # 49


## 41. Maximum Difference (j > i)




# Without inbuilt
def max_diff(arr):
    min_val, max_diff = arr[0], arr[1]-arr[0]
    for i in range(1,len(arr)):
        if arr[i]-min_val > max_diff:
            max_diff = arr[i]-min_val
        if arr[i] < min_val:
            min_val = arr[i]
    return max_diff

# With inbuilt
def max_diff_inbuilt(arr):
    min_val, max_diff = arr[0], float('-inf')
    for num in arr[1:]:
        max_diff = max(max_diff, num - min_val)
        min_val = min(min_val, num)
    return max_diff

print(max_diff([2,3,10,6,4,8,1]))         # 8
print(max_diff_inbuilt([2,3,10,6,4,8,1])) # 8


## 42. Next Greater Element

# Without inbuilt (stack O(n))
def next_greater(arr):
    n = len(arr)
    res = [-1]*n
    stack = []
    for i in range(n-1,-1,-1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(arr[i])
    return res

# With inbuilt (using enumerate and list comp)
def next_greater_inbuilt(arr):
    res, stack = [-1]*len(arr), []
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1] <= arr[i]: stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(arr[i])
    return res

print(next_greater([4,5,2,25]))         # [5,25,25,-1]
print(next_greater_inbuilt([4,5,2,25])) # [5,25,25,-1]


## 43. Next Smaller Element

# Without inbuilt
def next_smaller(arr):
    n = len(arr)
    res = [-1]*n
    stack = []
    for i in range(n-1,-1,-1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(arr[i])
    return res

# With inbuilt
def next_smaller_inbuilt(arr):
    res, stack = [-1]*len(arr), []
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1] >= arr[i]: stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(arr[i])
    return res

print(next_smaller([4,5,2,10,8]))         # [2,2,-1,8,-1]
print(next_smaller_inbuilt([4,5,2,10,8])) # [2,2,-1,8,-1]


## 44. Stock Buy and Sell

* **I (single transaction)**
* **II (multiple transactions)**
* **Cooldown (DP)**

# I: Single transaction
def max_profit_one(arr):
    min_price, max_profit = arr[0], 0
    for price in arr:
        if price < min_price: min_price = price
        if price-min_price > max_profit: max_profit = price-min_price
    return max_profit

# II: Multiple transactions
def max_profit_two(arr):
    profit = 0
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            profit += arr[i]-arr[i-1]
    return profit

# III: With cooldown (DP)
def max_profit_cooldown(prices):
    if not prices: return 0
    n = len(prices)
    hold, sold, rest = -prices[0], 0, 0
    for i in range(1,n):
        hold = max(hold, rest - prices[i])
        rest = max(rest, sold)
        sold = hold + prices[i]
    return max(sold, rest)

print(max_profit_one([7,1,5,3,6,4]))         # 5
print(max_profit_two([7,1,5,3,6,4]))         # 7
print(max_profit_cooldown([1,2,3,0,2]))      # 3


## 45. Kth Smallest / Largest
# Without inbuilt (Quickselect)
def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickselect(arr, low, high, k):
    if low <= high:
        pi = partition(arr, low, high)
        if pi == k: return arr[pi]
        elif pi < k: return quickselect(arr, pi+1, high, k)
        else: return quickselect(arr, low, pi-1, k)

def kth_smallest(arr, k):
    return quickselect(arr[:], 0, len(arr)-1, k-1)

# With inbuilt (heapq)
import heapq
def kth_smallest_inbuilt(arr, k):
    return heapq.nsmallest(k, arr)[-1]
def kth_largest_inbuilt(arr, k):
    return heapq.nlargest(k, arr)[-1]

print(kth_smallest([7,10,4,3,20,15], 3))         # 7
print(kth_smallest_inbuilt([7,10,4,3,20,15], 3)) # 7
print(kth_largest_inbuilt([7,10,4,3,20,15], 3))  # 10


## 46. Merge Intervals

# Without inbuilt
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])
    return merged

# With inbuilt
def merge_intervals_inbuilt(intervals):
    intervals.sort()
    res = []
    for s,e in intervals:
        if res and s <= res[-1][1]:
            res[-1][1] = max(res[-1][1], e)
        else:
            res.append([s,e])
    return res

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))         # [[1,6],[8,10],[15,18]]
print(merge_intervals_inbuilt([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]


## 47. Insert Interval

# Without inbuilt
def insert_interval(intervals, new_interval):
    res = []
    for i in range(len(intervals)):
        if intervals[i][1] < new_interval[0]:
            res.append(intervals[i])
        elif intervals[i][0] > new_interval[1]:
            res.append(new_interval)
            return res + intervals[i:]
        else:
            new_interval[0] = min(new_interval[0], intervals[i][0])
            new_interval[1] = max(new_interval[1], intervals[i][1])
    res.append(new_interval)
    return res

# With inbuilt (same logic but cleaner)
def insert_interval_inbuilt(intervals, new):
    res = []
    for s,e in intervals:
        if e < new[0]: res.append([s,e])
        elif s > new[1]:
            res.append(new); new=[s,e]
        else:
            new[0] = min(new[0], s); new[1] = max(new[1], e)
    res.append(new)
    return res

print(insert_interval([[1,3],[6,9]],[2,5]))         # [[1,5],[6,9]]
print(insert_interval_inbuilt([[1,3],[6,9]],[2,5])) # [[1,5],[6,9]]


## 48. Minimum Platforms (Trains)

# Without inbuilt
def min_platforms(arr, dep):
    arr.sort(); dep.sort()
    i=j=platforms=result=0
    while i<len(arr) and j<len(dep):
        if arr[i] <= dep[j]:
            platforms+=1; i+=1
            result = max(result, platforms)
        else:
            platforms-=1; j+=1
    return result

# With inbuilt (same but using zip)
def min_platforms_inbuilt(arr, dep):
    arr.sort(); dep.sort()
    i=j=plat=ans=0
    while i<len(arr) and j<len(dep):
        if arr[i]<=dep[j]: plat+=1; i+=1; ans=max(ans,plat)
        else: plat-=1; j+=1
    return ans

print(min_platforms([900,940,950,1100,1500,1800],[910,1200,1120,1130,1900,2000]))         # 3
print(min_platforms_inbuilt([900,940,950,1100,1500,1800],[910,1200,1120,1130,1900,2000])) # 3


## 49. Count Inversions

# Without inbuilt (merge sort O(n log n))
def merge_count(arr):
    if len(arr)<=1: return arr,0
    mid=len(arr)//2
    L,cL=merge_count(arr[:mid])
    R,cR=merge_count(arr[mid:])
    merged,i,j,c=[],0,0,0
    while i<len(L) and j<len(R):
        if L[i]<=R[j]: merged.append(L[i]); i+=1
        else: merged.append(R[j]); j+=1; c+=len(L)-i
    merged+=L[i:]+R[j:]
    return merged,c+cL+cR

def count_inversions(arr):
    return merge_count(arr)[1]

# With inbuilt (using sorted + bisect)
import bisect
def count_inversions_inbuilt(arr):
    seen=[]; inv=0
    for num in arr[::-1]:
        idx=bisect.bisect_left(seen,num)
        inv+=idx
        bisect.insort(seen,num)
    return inv

print(count_inversions([1,20,6,4,5]))         # 5
print(count_inversions_inbuilt([1,20,6,4,5])) # 5


## 50. Longest Consecutive Sequence

# Without inbuilt
def longest_consecutive(arr):
    arr_set = {}
    for num in arr: arr_set[num]=True
    max_len=0
    for num in arr:
        if num-1 not in arr_set:
            length=1
            while num+length in arr_set:
                length+=1
            max_len = max(max_len,length)
    return max_len

# With inbuilt (set trick)
def longest_consecutive_inbuilt(arr):
    nums=set(arr)
    max_len=0
    for num in nums:
        if num-1 not in nums:
            length=1
            while num+length in nums:
                length+=1
            max_len=max(max_len,length)
    return max_len

print(longest_consecutive([100,4,200,1,3,2]))         # 4
print(longest_consecutive_inbuilt([100,4,200,1,3,2])) # 4
