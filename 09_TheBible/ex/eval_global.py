
x=100
y=2
#print("global: ", globals())
#print("local: ", locals())

def test():

    def input(inp):
        print(inp)
    
    x=input("Welcome>>")
    z=2
    print(eval('input(123)',{"input":input,"y":2},{"z":1}))
    #print("global: ", globals())
    #print("local: ", locals())


test()
