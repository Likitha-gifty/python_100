# Check Whether a Number is a Prime or Not
# Method 1: Simple iterative solution

n= 12
count = 0
for i in range(2,n):
    if n % i == 0:
        count = 1
        break
if count == 1:
    print("not prime")
else:
    print("prime")


# Method 2: Optimization by break condition

n= 14
count = 0
if n < 2:
    count = 1
else:
    for i in range(2,n):
        print(n)
        if n % i == 0:
            count = 1
        break
    if count == 1:
        print("not prime")
    else:
        print("prime")

# Method 3: Optimization by n/2 iterations

n = 19
count = 0
if n < 2:
    count = 1
else:
    for i in range(2,int((n/2)+1)):
        if n % i == 0:
            count = 1
        break
    if count == 1:
        print("not prime")
    else:
        print("prime")




