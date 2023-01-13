"""
Write a python script to display all prime numbers within a range
range start = 15 end = 45
"""

# printing all prime numbers within the range 15 to 45
for e in range(15, 45) :
    i = 2
    while i < e :
        if e % i == 0 :
            break;
        i += 1
    if i == e :
        print(e, end=' ')