"""
Write a python script to print squares of first N natural numbers
"""

# taking input from the user
N = int(input("Enter a number : "))

# printing squares of first N natural numbers using range() in for loop
for e in range(1, N+1) :
    print(e**2)