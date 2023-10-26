# Set are another data structure available in python
# They are unordered
# They are mutable but only stores immutable elements
# They don't allow duplicates

# Creating a empty Set
# dummy_set = set()

# print(type(dummy_set))

# Creating a dataset
dataset = set()
 # or
dataset = set([1,2,3,4,67]) 
# print(type(dataset))


# dataset.add(1)
# print(dataset)

 # set associated methods
# print(dir(set))

# dataset.add(500)

# dataset.clear()

# return_var = dataset.pop()

# dataset.remove(500)
# print(dataset)

# second_copy = dataset
# second_copy.clear()

# first_copy = dataset.copy()
# first_copy.clear()
# print("dataset", dataset)
# print("firstcopy", first_copy)


# dataset.update([10, 9, 8])
# print(dataset)

# print(help(dataset.discard))

# dataset.remove(500)
# dataset.discard(500)
# print(return_var)
# print(dataset)
# print(first_copy)
second_dataset = {5, 6, 7,1,2,3,4}

# print(second_dataset)
# third = dataset.union(second_dataset)
# print(third, dataset, second_dataset)

copy_data = (dataset.intersection(second_dataset))
# print(copy_data)
# dataset.clear()
# dataset.update(copy_data)
print("dataset: ", dataset)
dataset.intersection_update(second_dataset)
print("dataset: ", dataset)
print("second_dataset: ", second_dataset)


# print(dataset.difference(second_dataset))
# print("before: ", dataset)
# print(second_dataset.difference_update(dataset))
# print("original dataset: ", dataset)
# print("second_dataset", second_dataset)

# print(dataset.symmetric_difference(second_dataset))
# print(second_dataset.symmetric_difference(dataset))
# print(second_dataset.symmetric_difference_update(dataset))

# print("Second dataset", second_dataset)


# print(help(set.symmetric_difference))

mydata = {1,2,3,4,5,6,7,8}
my2data = {50,60,8}
print("superset",mydata.issuperset(my2data))
print("subset",mydata.issubset(my2data))
print("disjoint",mydata.isdisjoint(my2data))














