# Jump statements
# They help us to jump the states in loops

# Continue - Helps in skipping
# Break - Helps to break the loop (Quit prematurely)

for item in range(10):
    if item%2==0:
        continue# skipping
    print(item)
    print()

for item in range(100):
    if item==50:
        break# Quitting
    print(item)
print('loop completed')
