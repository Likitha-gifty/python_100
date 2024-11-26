# Find the Sum of the First N Natural Numbers in Python
# Method 1 : Using for Loop

n=5
sum=0
for i in range(1,n+1,1):
    sum+=i
print(sum)

# Method 2 : Using Formula for the Sum of Nth Term

n=3
print(int(n*(n+1)/2))

# Method 3 : Using Recursion
def sum(n):
    if n ==1:
        return 1
    return n + sum(n-1)
n=5
print(sum(n))
