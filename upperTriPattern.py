n=int(input("enter the number of rows u need to print:"))

for i in range(0,n):
  print(" " * (n - i - 1) + "*" * (2 * i + 1))
