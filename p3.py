import numpy as np

print('The Options below shows different computations done to arrays and vectors.')
print('Enter the number corresponding to the function you would like to see. ')
print('\n1. Multiplication of two given arrays')
print('2. Outer Product of two given vectors')
print('3. The cross product of two given vectors')
print('4. Einstein’s summation convention of two given multidimensional arrays')

val = input()

p = [[2, 5], [6, 9]]
q = [[5, 4], [3, 6]]

a = np.array([2,4,6])
b = np.array([3,9,12])

#Multiplication of two given arrays
if val == '1':
	print("Original matrix:")
	print(p)
	print(q)
	result1 = np.dot(p, q)
	result2 = np.dot(q, p)
	print("Result of the two matrix multiplication:")
	print(result1)
	print(result2)

#Outer Product of two given vectors
elif val == '2':
	print("Original matrix:")
	print(p)
	print(q)
	result = np.outer(p, q)
	print("Outer product of the two vectors:")
	print(result)

#The cross product of two given vectors
elif val == '3':
	print("Original matrix:")
	print(p)
	print(q)
	result1 = np.cross(p, q)
	result2 = np.cross(q, p)
	print("Cross product of the two vectors(Vector 1, Vector 2):")
	print(result1)
	print("Cross product of the said two vectors(Vector 2, Vector 1):")
	print(result2)

#Einstein’s summation convention of two given multidimensional arrays
elif val == '4':
	print("Original 1-d arrays:")
	print(a)
	print(b)
	result =  np.einsum("n,n", a, b)
	print("Einstein’s summation convention of the said arrays:")
	print(result)
	x = np.arange(9).reshape(3, 3)
	y = np.arange(3, 12).reshape(3, 3)
	print("Original Higher dimension:")
	print(x)
	print(y)
	result = np.einsum("mk,kn", x, y)
	print("Einstein’s summation convention of the said arrays:")
	print(result)
else:
	print('Incorrect Entry! Please Try Again.')