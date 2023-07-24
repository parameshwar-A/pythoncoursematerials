
# List are ordered, mutable data structure
# Let's see each keyword
# Ordered meaning, the order of elements are maintained. Just like strings having index for characters.
# Mutable meaning, the elements of the string can be added/modified/removed.

name_list = ["paramesh", "Vijay", "Ajith", "Tom Hanks", "Robert Downey Jr"]

#name_list[0] = "Prakash"
name_list.insert(0,"prakash")
#print(f"Welcome {name_list[0]}")
#print(f"Welcome {name_list[1]}")
# The above is a list of names, in real time scenarios we encounter list of items every now and there.

# Let's say if we have multiple machines/servers under our infracture and we may need to perform some action on them, having list of them will come in handy while processing 

# Since they are iterable they are well worked with loops. So you can easily use it with loops

#for name in name_list:
#    print(f"Welcome {name}!")

#for ind in range(0, len(name_list)):
#    print(f"Welcome {name_list[ind]}")

# Lists in python don't have to contain same data types, I mean a single in python can have all variety of data types as elements

#data_set = [1, "My Name", 2.56, True]

# Even other data strucutres can also be stored inside this.

#data_set_1 = [["paramesh", "vijay"], ["hp", "lenovo"]]
#print(data_set_1[1][0])


# Methods associated with List

#print(dir(str))

# Appending - Add the given element to end of the list
#print("Before appending: ", name_list)
## Append takes exactly one argument
name_list.append("Tom Cruise") 
#
#print("After appending: ", name_list)


# Count - Returns the count of element in a list
product_list = [1000, 1100, 1200, 1100, 3000, 3200, 1100]
#print("Count of 1000: ", product_list.count(1000))


# Clear - Removes all items from the list ( Can be used to reset the list)
#print("Product list before clear: ", product_list)
#product_list.clear()
#print("Product list after clear: ", product_list)
#
# Reverse the order of the elements in the list
#print("Normal name list: ", name_list)
#name_list.reverse()
#print("name list after Reverse: ", name_list)

#name_list.append(["Hawk eye", "Natasha", "Dr.Banner"])
#print("after append", name_list)
#print(name_list[6])

# extent - Used to extend multiple items to the list
name_list.extend(["Hawk eye", "Natasha", "Dr.Banner"])
#name_list.extend("Hawk eye")
#print("After Extend :", name_list)
#print(name_list[8])

# index - Used to find the index of the element. Basically a find function

#print(name_list.index("Natasha"))


# Insert - Used to insert a element to particular location
#print("Name list before insert: ", name_list)
name_list.insert(7, "Wanda")
#print("Name list after insert: ", name_list)
#print(name_list.index("Natasha"))
# Due to inserting items in a particular location others are shifted towards right

# pop - Used to pop  the last element and return it to the user
#
#print("Popped element: ", name_list.pop())
#print("Name list after poping: ", name_list)
#
# Remove - Used to remove a particular element
#print(name_list.remove("Natasha"))
#print("Name list after removing: ", name_list)

# Sort
#name_list.sort(reverse=True)
#print(help(name_list.sort))
#print("Sorted list: ", name_list)

# copy - Used to create a copy of a list
# Call by reference
#first_copy = name_list
#print("Popped element: ", first_copy.pop())
#print("First copy: ", first_copy)
#print("Name List: ", name_list)

#second_copy = name_list.copy()
#print("Popped element: ", second_copy.pop())
#print("second copy: ", second_copy)
#print("Name List: ", name_list)

#

data=2
value=data
print(data, value)

value=3
print(data, value)








