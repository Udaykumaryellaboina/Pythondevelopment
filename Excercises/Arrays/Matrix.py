

# ✅ Matrix Problems (29–35)


## 29. Search in a Row-wise & Column-wise Sorted Matrix

# Without inbuilt (staircase search O(m+n))
def search_sorted_matrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    i, j = 0, cols - 1
    while i < rows and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return False

# With inbuilt (flatten + in operator)
def search_sorted_matrix_inbuilt(matrix, target):
    return any(target in row for row in matrix)

mat = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]
print(search_sorted_matrix(mat, 5))         # True
print(search_sorted_matrix_inbuilt(mat, 5)) # True


## 30. Rotate Matrix by 90 Degrees

# Without inbuilt (transpose + reverse rows)
def rotate_matrix(matrix):
    n = len(matrix)
    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse rows
    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
    return matrix

# With inbuilt (zip + slicing)
def rotate_matrix_inbuilt(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_matrix([row[:] for row in mat]))         # [[7,4,1],[8,5,2],[9,6,3]]
print(rotate_matrix_inbuilt(mat))                     # [[7,4,1],[8,5,2],[9,6,3]]


## 31. Print Matrix in Spiral Order

# Without inbuilt
def spiral_order(matrix):
    res = []
    top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
    while top <= bottom and left <= right:
        for i in range(left, right+1): res.append(matrix[top][i])
        top += 1
        for i in range(top, bottom+1): res.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left-1, -1): res.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1): res.append(matrix[i][left])
            left += 1
    return res

# With inbuilt (flatten trick + slicing loops)
def spiral_order_inbuilt(matrix):
    res = []
    while matrix:
        res += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix: res.append(row.pop())
        if matrix:
            res += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]: res.append(row.pop(0))
    return res

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_order([row[:] for row in mat]))        # [1,2,3,6,9,8,7,4,5]
print(spiral_order_inbuilt([row[:] for row in mat]))# [1,2,3,6,9,8,7,4,5]


## 32. Transpose of a Matrix

# Without inbuilt
def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transposed = [[0]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed

# With inbuilt (zip)
def transpose_inbuilt(matrix):
    return [list(row) for row in zip(*matrix)]

mat = [[1,2,3],[4,5,6]]
print(transpose(mat))        # [[1,4],[2,5],[3,6]]
print(transpose_inbuilt(mat))# [[1,4],[2,5],[3,6]]


## 33. Maximum Sum Submatrix

👉 This is the 2D Kadane’s Algorithm problem.

# Without inbuilt (2D Kadane O(n^3))
def max_sum_submatrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    max_sum = float('-inf')
    for left in range(cols):
        temp = [0]*rows
        for right in range(left, cols):
            for i in range(rows):
                temp[i] += matrix[i][right]
            # Apply 1D Kadane
            curr_sum = temp[0]
            best = temp[0]
            for i in range(1, rows):
                curr_sum = temp[i] if temp[i] > curr_sum+temp[i] else curr_sum+temp[i]
                best = best if best > curr_sum else curr_sum
            max_sum = max(max_sum, best)
    return max_sum

# With inbuilt (reuse sum() + max() for Kadane)
def max_sum_submatrix_inbuilt(matrix):
    rows, cols = len(matrix), len(matrix[0])
    max_sum = float('-inf')
    for left in range(cols):
        temp = [0]*rows
        for right in range(left, cols):
            temp = [temp[i]+matrix[i][right] for i in range(rows)]
            curr_sum = best = temp[0]
            for num in temp[1:]:
                curr_sum = max(num, curr_sum+num)
                best = max(best, curr_sum)
            max_sum = max(max_sum, best)
    return max_sum

mat = [[1,-2,-1,4],[2,3,4,-5],[-3,4,5,6]]
print(max_sum_submatrix(mat))        # 18
print(max_sum_submatrix_inbuilt(mat))# 18


## 34. Diagonal Sum of a Square Matrix

# Without inbuilt
def diagonal_sum(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        total += matrix[i][i]  # primary diagonal
        if i != n-i-1:
            total += matrix[i][n-i-1]  # secondary diagonal
    return total

# With inbuilt
def diagonal_sum_inbuilt(matrix):
    n = len(matrix)
    return sum(matrix[i][i] + (matrix[i][n-i-1] if i != n-i-1 else 0) for i in range(n))

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonal_sum(mat))        # 25
print(diagonal_sum_inbuilt(mat))# 25


## 35. Set Row & Column to Zero if an Element is Zero

# Without inbuilt
def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row_set, col_set = [], []
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_set.append(i)
                col_set.append(j)
    for i in range(rows):
        for j in range(cols):
            if i in row_set or j in col_set:
                matrix[i][j] = 0
    return matrix

# With inbuilt (set comprehension)
def set_zeroes_inbuilt(matrix):
    rows, cols = len(matrix), len(matrix[0])
    zero_rows = {i for i in range(rows) for j in range(cols) if matrix[i][j]==0}
    zero_cols = {j for i in range(rows) for j in range(cols) if matrix[i][j]==0}
    for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0
    return matrix

mat = [[1,2,3],[4,0,6],[7,8,9]]
print(set_zeroes([row[:] for row in mat]))        # [[1,0,3],[0,0,0],[7,0,9]]
print(set_zeroes_inbuilt([row[:] for row in mat]))# [[1,0,3],[0,0,0],[7,0,9]]
