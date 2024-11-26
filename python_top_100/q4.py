# Find the Sum of N Natural Numbers
# Method 1: Using for Loop

n,sum=6,0
for i in range(n+1):
    sum+= i
print(sum)

# Method 2: Using the Formula

number = 6
sum = int((number * (number + 1))/2)
print(sum)

# Method 3: Using Recursion

def recursum(number):
  if number == 0:
    return number
  return number + recursum(number-1)
number, sum = 6,0
print(recursum(number))