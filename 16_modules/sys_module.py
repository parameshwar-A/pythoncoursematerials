import sys

# Sys.stdin is used to read the standard input. 
#for line in sys.stdin:
#    print(line)
#    if line.rstrip() == "q":
#        break
#
# stderr - Write content to standard error stream
sys.stderr.write("My error message")

# stdout - Write content to standard output stream
sys.stdout.write("Welcome")

# argv - List of all command line arguments passed to this script.
# print(sys.argv)
# print(sys.orig_argv)


# Prints out the path variable of the OS. 
#print(sys.path)

# Prints out loaded modules. This may change based on execution
#print(sys.modules)
#import csv
#print("after ",sys.modules)


# GetSizeOf - Will return the size of the date stored in a variable or value in memory along with garbage collector.
#a=2
#name="welcome to the world"
#print(sys.getsizeof(name))

# Prints out which operating system the script currently running.
#print(sys.platform)

# Print all standard library modules that are present in standard lib. Even non applicable modules of that os will be listed. But they won't work.
#print(sys.stdlib_module_names)

#ps1 and ps2 
# only works in interpter interactive mode
#print(sys.ps1, sys.ps2)

