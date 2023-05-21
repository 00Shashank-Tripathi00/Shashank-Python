import math
def isPerfectSquare(x):
 s = int(math.sqrt(x))
 return s*s == x

def isFibonacci(n):
 return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

n = int(input("Enter a number: "))
if (isFibonacci(n) == True):
 print(n, "is a Fibonacci number")
else:
 print(n, "is not a Fibonacci number") 