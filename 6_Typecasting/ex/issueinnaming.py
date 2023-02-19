
# Let's say you are automatically deplying multiple containers.

# All containers in one account will be named like account name + instance_id 

# ex. Tata01, Tata02, Tata03 ....

account_name = input("Enter the name of the account: ")
instance_id = input("Enter the Id of the machine: ")

print(account_name+instance_id)
