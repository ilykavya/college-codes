# Experiment 4: Demonstrate all operators in Python

print("=" * 50)
print("1) ARITHMETIC OPERATORS")
print("=" * 50)

x, y = 17, 5
print(f"x = {x}, y = {y}")
print("Addition       x + y =", x + y)
print("Subtraction    x - y =", x - y)
print("Multiplication x * y =", x * y)
print("Division       x / y =", x / y)
print("Floor Division x // y =", x // y)
print("Modulus        x % y =", x % y)
print("Exponent       x ** y =", x ** y)

print("\n" + "=" * 50)
print("2) RELATIONAL (COMPARISON) OPERATORS")
print("=" * 50)

print("x == y:", x == y)
print("x != y:", x != y)
print("x > y :", x > y)
print("x < y :", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

print("\n" + "=" * 50)
print("3) ASSIGNMENT OPERATORS")
print("=" * 50)

a = 10
print("a =", a)

a += 5
print("a += 5 :", a)

a -= 3
print("a -= 3 :", a)

a *= 2
print("a *= 2 :", a)

a //= 4
print("a //= 4 :", a)

print("\n" + "=" * 50)
print("4) LOGICAL OPERATORS")
print("=" * 50)

p, q = True, False
print("p =", p, ", q =", q)
print("p and q:", p and q)
print("p or q :", p or q)
print("not p  :", not p)

print("\n" + "=" * 50)
print("5) BITWISE OPERATORS")
print("=" * 50)

m, n = 10, 4
print("m & n =", m & n)
print("m | n =", m | n)
print("m ^ n =", m ^ n)
print("~m =", ~m)
print("m << 1 =", m << 1)
print("m >> 1 =", m >> 1)

print("\n" + "=" * 50)
print("6) TERNARY OPERATOR (Conditional Expression)")
print("=" * 50)

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"age = {age}  status = {status}")

print("\n" + "=" * 50)
print("7) MEMBERSHIP OPERATORS")
print("=" * 50)

fruits = ["apple", "mango", "banana"]
print("fruits =", fruits)
print("'mango' in fruits   :", "mango" in fruits)
print("'grape' not in fruits:", "grape" not in fruits)

print("\n" + "=" * 50)
print("8) IDENTITY OPERATORS")
print("=" * 50)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2 (same content):", list1 == list2)
print("list1 is list2 (different objects):", list1 is list2)
print("list1 is list3 (same object):", list1 is list3)









# Sample Output:

# 1) ARITHMETIC OPERATORS

# x = 17, y = 5
# Addition       x + y = 22
# Subtraction    x - y = 12
# Multiplication x * y = 85
# Division       x / y = 3.4
# Floor Division x // y = 3
# Modulus        x % y = 2
# Exponent       x ** y = 1419857

# 2) RELATIONAL (COMPARISON) OPERATORS

# x == y: False
# x != y: True
# x > y : True
# x < y : False
# x >= y: True
# x <= y: False

# 3) ASSIGNMENT OPERATORS

# a = 10
# a += 5 : 15
# a -= 3 : 12
# a *= 2 : 24
# a //= 4 : 6

# 4) LOGICAL OPERATORS

# p = True, q = False
# p and q: False
# p or q : True
# not p  : False

# 5) BITWISE OPERATORS

# m & n = 0
# m | n = 14
# m ^ n = 14
# ~m = -11
# m << 1 = 20
# m >> 1 = 5

# 6) TERNARY OPERATOR

# age = 20  status = Adult

# 7) MEMBERSHIP OPERATORS

# fruits = ['apple', 'mango', 'banana']
# 'mango' in fruits    : True
# 'grape' not in fruits: True

# 8) IDENTITY OPERATORS

# list1 == list2: True
# list1 is list2: False
# list1 is list3: True
