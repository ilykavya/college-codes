# Experiment 5: Add and multiply complex numbers
c1 = complex(input("Enter first complex number (e.g. 3+4j): "))
c2 = complex(input("Enter second complex number (e.g. 1+2j): "))
sum_result = c1 + c2
prod_result = c1 * c2
print("\nFirst complex number:", c1)
print("Second complex number:", c2)
print("Addition c1 + c2 =", sum_result)
print("Multiplication c1 * c2 =", prod_result)
print("\nReal part of sum:", sum_result.real)
print("Imaginary part of sum:", sum_result.imag)



# Sample Output:
# Enter first complex number (e.g. 3+4j): 3+4j
# Enter second complex number (e.g. 1+2j): 1+2j
# First complex number: (3+4j)
# Second complex number: (1+2j)
# Addition c1 + c2 = (4+6j)
# Multiplication c1 * c2 = (-5+10j)
# Real part of sum: 4.0
# Imaginary part of sum: 6.0
