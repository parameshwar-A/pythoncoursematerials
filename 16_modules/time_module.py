import time

#print current time in floating point number not in normal format
print(time.time())

#print current timezone you are in floating point number
print(time.timezone)

#Format the current time object into a regular usable format of your choice
print(time.strftime("%H:%M:%S"))

# Used to create a time object based on your text based input
print(time.strptime("07:08:10","%H:%M:%S"))

# sleep will render the time as idle.
# For example in some part of the code you may need to wait for some time to move to next process. In that case how do you cause delay in starting. 

# Sleep help you to buy time before going to next line.
#print("hello")
#time.sleep(10)
#print("world")

print(time.get_clock_info("monotonic"))
print(time.CLOCK_MONOTONIC)

print(time.localtime())


