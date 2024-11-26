# Find the Sum of the Numbers in a Given Interval in Python Language
# Method 1: Using Brute Force


n1,n2= 2,5
sum = 0
for i in range(n1,n2+1):
    sum += i
print(sum)

# Method 2: Using the Formula
n1,n2= 3,6
sum=int((n2*(n2+1)/2)- (n1*(n1+1)/2)+n1)
print(sum)

# Method 3: Using Recursion

def recursum(sum,num1,num2):
  if num1 > num2:
    return sum
  return num1 + recursum(sum,num1+1,num2)

num1, num2 = 3, 6
sum = 0
print(recursum(sum,num1,num2))
