# format

name="paramesh"
age = "23"
place = "kanchipuram"

# print(f"hello {name} your age is {age} and you are from {place}")

# print("hello {} your age is {} and you are from {}".format(age,name, place))

# print("welcome {name} to {place}".format(name="paramesh",place= "world"))
# print("welcome {0} to {1}".format("paramesh", "world"))
# print("welcome {} to {}".format("paramesh","world"))

# print("amount {:,}".format(1000000))
# print("amount {:e}".format(1000000))
# print("amount {:x}".format(1000000))
# print("amount {:.4f}".format(1000000.0000000))

# encode
# print("amount".encode("utf_32"))
# print("amount".encode("utf_8"))

# removeprefix
# print("superawesomesup".removeprefix("sup"))

# removesuffix
# print("superawesome".removesuffix("some"))


# splitlines
# '' or " "
# data = """
# welcome 
# to 
# the
# moon
# """

# mydata = "welcome\nto\nmy\nmoon"
# print(mydata)
# print(data.splitlines())
# print(mydata.splitlines())


# Maketrans and translate
# table = str.maketrans("a b c d e","1 2 3 4 10")
# # {
# # a : w
# # b : x
# # c : y
# # d : z
# # }
# print(table)
print("abcd".translate({97:120}))












