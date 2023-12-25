
# conditional logic expression
n = input()
n = int(n)

# even odd no find out
"""
if n >= 0:
    print(n, "is positive")
else:
    print(n, "is negative")
"""
if n >= 0 and n % 2 == 0:
    print(n, "is positive and even number")
elif n >= 0 and n % 2 == 1:
    print(n, "is positive and odd number")
elif n < 0 and n % 2 == 0:
    print(n, "is negative and even number")
else: 
    print(n, "is negative and odd number")

"""
if n >= 0:
    if n % 2 == 0:
        print(n, "is positive and even number")
    else:
        print(n, "is positive and ood number")
else:
    if n % 2 == 0:
        print(n, "is negative and even number")
    else:
        print(n, "is negative and odd number")

"""        

"""
if n % 2 == 0:
    print(n, "is even")
else:
    print(n, "is odd")
"""