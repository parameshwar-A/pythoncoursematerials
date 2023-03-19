# For Loops
# used when exact number of iteration is determined the start and stop

#for num in range(0,10):
#    print(num)

# Let's take a deep look

# range(0, 10) --> will give iteratable numbers of 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 
# Important Note: Just like slicing ending won't be included. (n-1) will be the final item

# num variable is a iteration variable which takes values for every completion of loop.
# For first run it will have 0, in second run it will have 1, so on...

# The range function also has a step value just like string slicing syntax

#range(start, stop, step) Default step size is 1
for num in range(0,10,2):
    print(num)
