
print("hello ullagam!")

print("Welcome", "to", "the", "world", sep="\n")

print("Welcome", end=" ")
print("to", end=" ")
print("the", end=" ")
print("word", end=" ")

#help(print)
outlog=open("outlog.txt", "w")
print("The log starts here!", file=outlog)
outlog.close()
