n = int(input("Enter the number of rows you need to print: "))

for i in range(n - 1, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
