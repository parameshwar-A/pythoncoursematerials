import random

# Function without param without return
def divider():
    print("#"*20)
    

# Function with param without return
def message_printer(msg):
    print("#"*20)
    print(msg.center(20))
    print("#"*20)


# Function without param with return
def random_generator():
    return random.random()



# Function with param with return
def addition(a, b):
    return a+b
