# Tuple

# Ordered
# Immutable
# Allows duplicates 

# Tuple is very similar to list but tuple is immutable meaning you cannot add or remove elements after initial assignment.

#scores = (1, 2, 3, 4, 1, 1)
scores = tuple(range(0,9, 1))
#print(dir(scores))
#print(type(scores))
#print(scores)
# See tuple syntax is different from list because tuple uses paranthesis not square brackets

# Since tuple is immutable it has less built-in methods associated with it

# Count

#print(scores.count(2))

# Returns a count of the particular value passed

# Index - Returns the first index value of the element passed
#print(scores.index(8))
print(scores)
print("Before list converstion", type(scores))

scores=list(scores)
print("Before insert ", type(scores))
scores.insert(0,1999)

scores=tuple(scores)
print("At the end", type(scores))
print(scores)













