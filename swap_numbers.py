#method1_Pythonic way
a=int(input("enter first number (a):"))
b=int(input("enter seecond number (b):"))
print("\nbefore swapping:a=",,",b=",b)
a,b=b,a
print("after swapping:a=",a,",b=",b)

#method2_arithmetic way
a=int(input("enter first number (a):"))
b=int(input("enter seecond number (b):"))
print("\nbefore swapping:a=",,",b=",b)
a=a+b
b=a-b
a=a-b
print("after swapping:a=",a,",b=",b)



#sample output
#enter the first number (a):25
#enter seecond number (b):40
#before swapping:a=25,b=40
#after swapping:a=40,b=25
