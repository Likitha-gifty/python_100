# Check if a Number is Positive and Negative in Python
# Method 1: Using Brute Force

n = -10
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


# Method 2: Using Nested if-else Statements

n = -1
if n >= 0:
    if n ==0:
        print("Positive")
    else:
        print("Positive")
else:
    print("Negative")

# Method 3: Using Ternary Operator

n = 10
print("positive") if n>=0 else print("Negative")