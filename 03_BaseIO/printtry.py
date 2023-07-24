#this is to print hello ullagam

#print(1,2,3,"sundar")

#print(1, 2, 3, 4,"string",sep=",")
#\n newline
#\t tab

#print("Welcome", "to", "the", "world", sep="\n")
#print("hello","world1",sep="$",end=" ")  #end default value "\n"
#print("world")


#print("welcome", end=" ")
#print("hello", end=" ")
#print("Welcome", end=" ")
#print("to", end=" ")
#print("the", end=" ")
#print("word")
#print(1,2,3,4, sep="$", end="@")
#help(print)
outlog=open("sundar.txt", "w")
print("The log starts here!", file=outlog)
outlog.close()
