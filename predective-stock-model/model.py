import csv
import numpy as np 
from sklearn.svm import SVR
import matplotlib.pyplot as plt 
dates = []
prices = []
def get_data(filename):
	with open(filename,'r') as csvFile:
		csvFileReader = csv.reader(csvFile)
		next(csvFileReader)
		for row in csvFileReader:
			dates.append(int(row[2].split("-")[0]))
			prices.append(float(row[4]))
	return
def predict_prices(dates, prices, x):
	dates = np.reshape(dates,(len(dates),1))

	svr_lin = SVR(kernel='linear', C=1e3)
	svr_poly = SVR(kernel='poly',C=1e3, degree=2)
	svr_rbf = SVR(kernel='rbf',C=1e3, gamma=0.1)

	svr_rbf.fit(dates, prices)
	svr_poly.fit(dates, prices)
	svr_lin.fit(dates, prices)

	plt.scatter(dates, prices, color='black', label='Data')
	plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF')
	plt.plot(dates, svr_lin.predict(dates), color='blue', label='Linear Model')
	plt.plot(dates, svr_poly.predict(dates), color='green', label='Poly')
	plt.xlabel('date')
	plt.ylabel('price')
	plt.legend()
	plt.show()

	return svr_poly.predict(x)[0], svr_rbf.predict(x)[0], svr_lin.predict(x)[0] 

get_data('icici2.csv')
predicted_prices = predict_prices(dates, prices,21)
print((predicted_prices[1] + predicted_prices[2])/2)
print(predicted_prices)