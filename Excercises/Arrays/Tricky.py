

# ✅ Miscellaneous / Tricky Array Problems (51–60)


## 51. Rearrange Positive and Negative Numbers Alternately

# Without inbuilt
def rearrange_pos_neg(arr):
    pos, neg = [], []
    for x in arr:
        if x >= 0: pos.append(x)
        else: neg.append(x)
    res, i, j = [], 0, 0
    while i < len(pos) and j < len(neg):
        res.append(pos[i]); res.append(neg[j])
        i += 1; j += 1
    res.extend(pos[i:]); res.extend(neg[j:])
    return res

# With inbuilt (list comprehensions)
def rearrange_pos_neg_inbuilt(arr):
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    res = [None]*(len(pos)+len(neg))
    res[::2], res[1::2] = pos, neg
    return [x for x in res if x is not None]

print(rearrange_pos_neg([1,-2,3,-4,5,-6]))         
print(rearrange_pos_neg_inbuilt([1,-2,3,-4,5,-6]))


## 52. Rearrange in Wave Form

# Without inbuilt
def wave_form(arr):
    n = len(arr)
    for i in range(0,n-1,2):
        if arr[i] < arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr

# With inbuilt
def wave_form_inbuilt(arr):
    arr.sort()
    for i in range(0,len(arr)-1,2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

print(wave_form([3,6,5,10,7,20]))
print(wave_form_inbuilt([3,6,5,10,7,20]))


## 53. Rearrange so that `arr[i] = i`

# Without inbuilt
def rearrange_index(arr):
    n = len(arr)
    res = [-1]*n
    for i in range(n):
        if 0 <= arr[i] < n:
            res[arr[i]] = arr[i]
    return res

# With inbuilt
def rearrange_index_inbuilt(arr):
    n = len(arr)
    return [i if i in arr else -1 for i in range(n)]

print(rearrange_index([-1,-1,6,1,9,3,2,4,-1]))
print(rearrange_index_inbuilt([-1,-1,6,1,9,3,2,4,-1]))


## 54. Maximum Circular Subarray Sum

# Without inbuilt (Kadane + wrap case)
def kadane(arr):
    max_end = max_so = arr[0]
    for x in arr[1:]:
        max_end = x if x > max_end+x else max_end+x
        max_so = max_so if max_so > max_end else max_end
    return max_so

def circular_subarray_sum(arr):
    max_kadane = kadane(arr)
    total, min_end, min_so = 0, arr[0], arr[0]
    for x in arr:
        total += x
    for x in arr[1:]:
        min_end = x if x < min_end+x else min_end+x
        min_so = min_so if min_so < min_end else min_end
    if min_so == total: return max_kadane
    return max(max_kadane, total - min_so)

# With inbuilt
def circular_subarray_sum_inbuilt(arr):
    total = sum(arr)
    max_sum, cur, min_sum, cur_min = arr[0], arr[0], arr[0], arr[0]
    for x in arr[1:]:
        cur = max(x, cur+x); max_sum = max(max_sum, cur)
        cur_min = min(x, cur_min+x); min_sum = min(min_sum, cur_min)
    return max_sum if max_sum < 0 else max(max_sum, total-min_sum)

print(circular_subarray_sum([5,-3,5]))         
print(circular_subarray_sum_inbuilt([5,-3,5]))


## 55. Leaders in an Array

# Without inbuilt
def leaders(arr):
    n = len(arr)
    max_from_right = arr[-1]
    res = [max_from_right]
    for i in range(n-2,-1,-1):
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            res.append(arr[i])
    return res[::-1]

# With inbuilt
def leaders_inbuilt(arr):
    res, max_so = [], float('-inf')
    for x in reversed(arr):
        if x > max_so:
            res.append(x)
            max_so = x
    return res[::-1]

print(leaders([16,17,4,3,5,2]))         
print(leaders_inbuilt([16,17,4,3,5,2]))


## 56. Find Peak Element

# Without inbuilt (binary search O(log n))
def peak_element(arr):
    l,r=0,len(arr)-1
    while l<r:
        mid=(l+r)//2
        if arr[mid] < arr[mid+1]:
            l=mid+1
        else:
            r=mid
    return l

# With inbuilt (max index)
def peak_element_inbuilt(arr):
    return arr.index(max(arr))

print(peak_element([1,2,1,3,5,6,4]))
print(peak_element_inbuilt([1,2,1,3,5,6,4]))


## 57. Cyclically Rotate by One

# Without inbuilt
def rotate_by_one(arr):
    last = arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = last
    return arr

# With inbuilt
def rotate_by_one_inbuilt(arr):
    return [arr[-1]] + arr[:-1]

print(rotate_by_one([1,2,3,4,5]))
print(rotate_by_one_inbuilt([1,2,3,4,5]))


## 58. Move All Zeros to End

# Without inbuilt
def move_zeros(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
    return arr

# With inbuilt
def move_zeros_inbuilt(arr):
    return [x for x in arr if x != 0] + [0]*arr.count(0)

print(move_zeros([0,1,0,3,12]))
print(move_zeros_inbuilt([0,1,0,3,12]))


## 59. Smallest Missing Positive Integer

# Without inbuilt (O(n) using index marking)
def first_missing_positive(arr):
    n=len(arr)
    for i in range(n):
        while 1<=arr[i]<=n and arr[arr[i]-1]!=arr[i]:
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
    for i in range(n):
        if arr[i]!=i+1: return i+1
    return n+1

# With inbuilt (set trick)
def first_missing_positive_inbuilt(arr):
    s=set(arr)
    i=1
    while i in s: i+=1
    return i

print(first_missing_positive([3,4,-1,1]))
print(first_missing_positive_inbuilt([3,4,-1,1]))


## 60. Implement Array with Dynamic Memory (simulate resizing)

# Without inbuilt
class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.arr = [None]*self.capacity
    
    def resize(self):
        self.capacity *= 2
        new_arr = [None]*self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
    
    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = value
        self.size += 1
    
    def __str__(self):
        return str(self.arr[:self.size])

# With inbuilt (just list)
class DynamicArrayInbuilt:
    def __init__(self):
        self.arr=[]
    def append(self,value):
        self.arr.append(value)
    def __str__(self):
        return str(self.arr)

da = DynamicArray()
for i in range(6): da.append(i)
print(da)

db = DynamicArrayInbuilt()
for i in range(6): db.append(i)
print(db)
