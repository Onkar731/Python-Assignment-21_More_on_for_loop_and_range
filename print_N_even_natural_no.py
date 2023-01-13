"""
Write a python script to print first N even natural numbers
"""

# taking input from the user
N = int(input("Enter a number : "))

# printing first N even natural numbers
for e in range(1, N+1) :
    print(e*2)
    
# another logic
"""
    for e in range(2, N*2+1, 2) :
        print(e)
"""