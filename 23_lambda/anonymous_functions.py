# Anonymous functions
# Lambda's are anonymous functions These are similar to normal functions but don't have seperate function defenintions

# lambda function can be stored into a variable
func = lambda x: x*2

print(func(2))


# You can have multiple parameters too!

func2 = lambda x,y: y*2+x*2

print(func2(3,4))

# You can also have optional parameters

func3 = lambda x,y=5: x+y

print(func3(2))
print(func3(3,5))


# You can't have multiple outputs

func4 = lambda x: (x**2,x*2)

print(func4(2))

#But the workaround can be using a datastructure to wrap the multiple params in it!
