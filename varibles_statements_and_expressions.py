#2 VARIBLES STATEMENTS AND EXPRESSIONS



# Example 1: Creating and Changing Variables

name = "kavya"
age = 18
height = 5.4
print(name)
print(age + 1)
# Change the value
age = 19
print("Next year age will be", age)
# Multiple assignment
x, y, z = 10, 20, 30
print(x, y, z)

# Output:
# kavya
# 19
# Next year age will be 20
# 10 20 30




# Example 2: Statements vs Expressions

age = 19
name = "kavya"
# Expressions
result = 15 + 7 * 2
is_adult = age >= 18
greeting = "Hi " + name
print(result)
print(is_adult)
print(greeting)
# Statement
print("This is a statement")
# if statement
if age >= 18:
    print("Adult")

# Output:
# 19
# True
# Hi kavya
# This is a statement
# Adult







#EXERCISES--------------


# Exercise 1: Create and Print Variables

name = "kavya"
age = 19
height = 5.4
print(name)
print(age)
print(height)

# Output:
# kavya
# 19
# 5.4



# Exercise 2: Calculate Average

avg = (45 + 67 + 89) / 3
print(avg)

# Output:
# 67.0





# Exercise 3: Swap Two Variables

a = 5
b = 10
a, b = b, a
print(a)
print(b)

# Output:
# 10
# 5




# Exercise 4: Statements and Expressions

x = 10
print(3 * 4 + 2)
print("Hello")
print(len("Python"))

# Output:
# 14
# Hello
# 6

# Statements:
# x = 10
# print("Hello")

# Expressions:
# 3 * 4 + 2
# len("Python")
