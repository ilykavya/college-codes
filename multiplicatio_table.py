#experiment 6:Multiplication table of a given number
num = int(input("Enter a number to print its table : "))
print(f"Multiplication Table of {num}")
for i in range(1, 11):
    print(f"{num} x {i:2} : {num * i}")

# Sample Output:
# Enter a number to print its table : 7
# Multiplication Table of 7
# 7 x  1 : 7
# 7 x  2 : 14
# 7 x  3 : 21
# 7 x  4 : 28
# 7 x  5 : 35
# 7 x  6 : 42
# 7 x  7 : 49
# 7 x  8 : 56
# 7 x  9 : 63
# 7 x 10 : 70
