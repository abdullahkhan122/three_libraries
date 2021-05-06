import cv2
import matplotlib.pyplot as plt

print('\nWelcome to the guessing game.')
print('Three out of the total four pieces of an image will be shown.')
print('Guess the image by entering the number correspondng to the location.')

photo = cv2.imread('gw_bridge.jpg')

start = input('Press Enter To Continue ')
print('')

if start == '':

	plt.imshow(photo[0:300, 0:400])
	plt.show()

	plt.imshow(photo[300:600, 400:1000])
	plt.show()

	plt.imshow(photo[0:300, 400:1000])
	plt.show()

	print('1. WaterFall')
	print('2. Bridge')
	print('3. Mountain')
	print('4. Airplane')

	test = input("Enter you response: ")

	if test == '2':
		print('You Win!')
		plt.imshow(photo)
		plt.show()
	else:
		print('Incorrect, Try Again')
else:
	print('Try Again and Press Enter')
