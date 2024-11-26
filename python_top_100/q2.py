# q2.py
# Placeholder for even/odd check functionality
num = 17
print("Even") if num%2 == 0 else print("Odd")

#bitwise operator
def isEven(num):
  return not num&1

if __name__ == "__main__":
  num = 13
  if isEven(num):
    print('Even')
  else:
    print('Odd')