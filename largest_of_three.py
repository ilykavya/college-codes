num1=float(input("enter first number:"))
num1=float(input("enter second number:"))
num1=float(input("enter third number:"))
if num1>=num2 and num1>=num3:
  largest=num1
elif num2>=num1 and num2>=num3:
  largest =num2
else:
  largest=num3
  print("the largest number is",largest)
  
#sample Output
#enter first number:45
#enter second number:78
#enter third number:23
#the largest number is :78.0
