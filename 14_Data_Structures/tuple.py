# Tuple

# Ordered
# Immutable
# Allows duplicates 

# Tuple is very similar to list but tuple is immutable meaning you cannot add or remove elements after initial assignment.

scores = (1, 2, 3, 4, 1, 1)
#scores = ()
# print(scores, type(scores))
names = ["paramesh", "arun", "paramesh"]

#scores = tuple()
# scores = tuple(range(0,9, 1))
#print(scores, type(scores))
scores = tuple(range(0,9, 1))
print(dir(scores))
#print(scores.__doc__)
#print(help(tuple))
#print(scores)
#print(scores)
# See tuple syntax is different from list because tuple uses paranthesis not square brackets

# Since tuple is immutable it has less built-in methods associated with it

# Count

# print(scores.count(1))

# Returns a count of the particular value passed

# Index - Returns the first index value of the element passed
# print(scores.index(5))
print(scores)
print("Before list converstion", type(scores))

scores=list(scores)
print("Before insert ", type(scores))
scores.insert(0,1999)

scores=tuple(scores)
print("At the end", type(scores))
print(scores)













