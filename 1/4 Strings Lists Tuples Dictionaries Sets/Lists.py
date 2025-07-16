#✅ Python list Basics
#🔹 Definition

my_list = [1, 2, 3, 'apple', [4, 5]]
#✅ Ordered (maintains insertion order)

#✅ Mutable (can change items)

#✅ Allows duplicates

#✅ Can be nested

#🧰 Common Built-in Methods of Lists
#Here’s a categorized list of commonly used list methods:
'''
Method	            Description	                                                        Example
append(x)	        Adds x to the end of the list	                                    lst.append(5)
extend(iterable)	Adds all elements from another iterable (like a list, tuple)        lst.extend([6, 7])
insert(i, x)	    Inserts x at index i	                                            lst.insert(1, 'apple')
remove(x)	        Removes first occurrence of x	                                    lst.remove('apple')
pop([i])	        Removes and returns item at index i (last item if i not given)	    lst.pop()
clear()	            Removes all items from the list                                 	lst.clear()
index(x[, start])	Returns the index of first occurrence of x	                        lst.index(3)
count(x)	        Counts how many times x appears	                                    lst.count(2)
sort()	            Sorts the list in place (ascending by default)	                    lst.sort()
reverse()	        Reverses the list in place	                                        lst.reverse()
copy()	            Returns a shallow copy of the list	                                new_list = lst.copy()

📌 Examples'''

lst = [3, 1, 4, 1, 5]

lst.append(9)        # [3, 1, 4, 1, 5, 9]
lst.extend([2, 6])   # [3, 1, 4, 1, 5, 9, 2, 6]
lst.insert(2, 7)     # [3, 1, 7, 4, 1, 5, 9, 2, 6]
lst.remove(1)        # [3, 7, 4, 1, 5, 9, 2, 6]
value = lst.pop()    # 6 (removed), lst now: [3, 7, 4, 1, 5, 9, 2]
idx = lst.index(9)   # 5
cnt = lst.count(1)   # 1
lst.sort()           # [1, 2, 3, 4, 5, 7, 9]
lst.reverse()        # [9, 7, 5, 4, 3, 2, 1]

"""🧠 Tips
Use sorted(lst) if you want a new sorted list without modifying the original.

Use copy() or slicing (lst[:]) to make copies and avoid reference issues.

Lists can store mixed data types, but doing so may cause issues with sorting or arithmetic."""

