from collections import deque

my_dq = deque([1,2,3,4,5,6,7,8,9,0],10)
# Deque takes two one iterable and second as max len
# Length is optional if given creates a limited deque otherwise growing one.

#print("Intial: ",my_dq)

#Append same as list, add element to right of the deque
#my_dq.append(199)
#print(my_dq)


# Append left, just same as append but in the left side of the deque
#my_dq.appendleft(10)
#print(my_dq)

# Note when appending/Inserting more items than the max len of deque.
# Items will be dropped in the opposite side of appending or inserting.

# Clear same as we saw in list and other data structure
#my_dq.clear()
#print(my_dq)

# copy - same as we did in list. Won't affect the parent if we made this type of copy.
#sec_dq = my_dq.copy()
#sec_dq.clear()
#print("parent one: ",my_dq,"copied", sec_dq)


# count - returns the count of element given in the deque
#print(my_dq.count(0))


# Extend - Merging two iterables same as list.
#my_dq.extend((100,200,300))
#print(my_dq)

# ExtendLeft - Same extend but in left direction
#my_dq.extendleft((100,200,300))
#print(my_dq)

# Make sure you understand the trend of extendign in deques!

# Insert - Works also same as list, insert the element in the specified index.
#my_dq.pop()
#my_dq.insert(0, 9999)
#print(my_dq)

# Note: Raises index error when max len is already attained in deque


# index - Also same as list
# Return positional index of given element in deque
print(my_dq.index(5))


# pop - removes an element from right and returns it
#my_dq.pop()
#print(my_dq)

# popleft - Same as pop but in left direction
#my_dq.popleft()
#print(my_dq)

# Remove - removes an element mentioned from the deque
#my_dq.remove(0)
#print(my_dq)

# Reverse - Reverse elements in a deque based on the index 
#my_dq.reverse()
#print(my_dq)

# Rotate - Rotate the deque based on the number you give
#my_dq.rotate(3)
#print(my_dq)
# If number given in -ve it will rotate in left direction


