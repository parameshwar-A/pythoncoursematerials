#this is to print hello ullagam
#print(1,2,3,4,"string")

#print("Welcome", "to", "the", "world", sep="\n")

#print("welcome", end=" ")
#print("hello",end=" ")
#print("Welcome", end=" ")
#print("to", end=" ")
#print("the", end=" ")
#print("word", end=" ")
#print(1,2,3,4, sep="$", end="@")
#help(print)
outlog=open("vijay.txt", "w")
print("The log starts here!", file=outlog)
outlog.close()
