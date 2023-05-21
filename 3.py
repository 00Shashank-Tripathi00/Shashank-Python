def findPosiƟon(k, n):
 f1 = 0
 f2 = 1
 i = 2
 while i!=0:
 f3 = f1 + f2
 f1 = f2
 f2 = f3
 if f2%k == 0:
 return n*i
 i += 1
 return
k = int(input("Enter a number: "))
n = int(input("Enter the posiƟon of the mulƟple: "))
print("The", n, "th mulƟple of", k, "in the Fibonacci Series is", findPosiƟon(k, n))
