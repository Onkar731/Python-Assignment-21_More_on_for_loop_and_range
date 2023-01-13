"""
Write a python script to print first N odd natural numbers
"""

# taking input from the user
N = int(input("Enter a number : "))

# printing first N odd natural numbers
for e in range(1, N+1) :
    print(e*2-1)

# another logic
"""
    for e in range(1, N*2, 2) :
        print(e) 
"""