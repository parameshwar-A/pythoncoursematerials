import random

# randint will help to give a random integer from a lower and upper limit
# note those limits are also included
print(random.randint(0,20))

# Random will give you a random number between 0 and 1
print(random.random())

# RandRange will give you random number from range of value just like range in loops
# you will have start, stop and step

print(random.randrange(0,20,2))
# For above line of code you will always get random even number between 0 and 20 

# sample will give us a sample of the given population(aka given data)
print(random.sample([1,2,3,4,5,6], 1))

# if you have duplicates in sample also you can create them easily
print(random.sample([2,40], counts=[5,6], k=4))
# [2, 2, 2, 2, 2, 40, 40, 40, 40, 40, 40]

# choice is used to get a random output from a sequence of elements

print(random.choice([1,10,100,1000,10000,100000]))

# choices is more like choice but with more elements and with weightage for those

print(random.choices([1,2,3,4,5,6,7,8],weights=[0,0,2,0,1,1,0,0], k=3))

print(random.choices(data,cum_weights=[10,0,1,0,0,0,0,8],k=3))

#if both weights are given it will throw type error and if we have zero weights it throws valueerror

#shuffle
# Shuffle sequence in place so it will not return just update the source itself
data = [1, 2, 3, 4, 5, 6, 7, 8]
# Before shuffle
print(data)
print(data[0])

#Doing shuffle
random.shuffle(data)

#After shuffle
print(data)
print(data[0])

#Randombyte generator

print(random.randbytes(2))
#based on the n parameter passed we get n number of bytes

