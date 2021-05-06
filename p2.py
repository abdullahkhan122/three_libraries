import pandas as pd
import matplotlib.pyplot as plt
  
print('The following data will show the number of \nCovid-19 Cases of the top nine states in the US\n')
val = input('To view it in DataFrame, press 1\nTo view it in a Scatterplot, press 2: ')


if val > '2':
	print('Incorrect Entry! Try Again.')

dataframe = pd.read_csv('covidcases.csv')

if val == '1':  
	df = pd.DataFrame({
		'state':['California', 'Texas', 'Florida', 'New York', 
		'Illinois', 'Pennsylvania', 'Georgia', 'Ohio', 'New Jersey'],
		'cases':[3722141, 2859611, 2178783, 2008514, 1306690, 1116044
				,1086473, 1056606, 983875]

	})

	print(df)


if val == '2':
	fig = plt.figure(figsize=(10, 5))
	x = dataframe.State
	y = dataframe.Cases
	plt.gca().invert_yaxis()
	plt.xticks(rotation=45)
	plt.title('Covid Cases In The US')
	plt.xlabel('States')
	plt.ylabel('Cases')
	plt.scatter(x,y)
	plt.show()