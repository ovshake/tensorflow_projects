import bs4 as bs
import datetime as dt 
import pandas as pd 
import os 
import pandas_datareader.data as web 
import matplotlib.pyplot as plt
import requests
import pickle
def save_sp500_ticker():
	resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
	soup = bs.BeautifulSoup(resp.text,'lxml')
	table = soup.find('table', {'class':'wikitable sortable'})
	tickers = []
	for row in table.findAll('tr')[1:]:
		ticker = row.findAll('td')[0].text
		tickers.append(ticker)
	with open('sp500ticker.pickle',"wb") as f:
		pickle.dump(tickers,f)
	print(tickers)

# save_sp500_ticker()
# def get_data_from_yahoo(reloadData=False):
# 	if reloadData:
# 		save_sp500_ticker()
# 	else:
# 		with open('sp500ticker.pickle','rb') as f:
# 			tickers = pickle.load(f)
# 		if not os.path.exists('stock_dfs'):
# 			os.makedirs('stock_dfs')
# 		start = dt.datetime(2000,1,1)
# 		end = dt.datetime(2016,12,31)
# 		for ticker in tickers:
# 			print(ticker)
# 			if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
# 				try:
# 					df = web.DataReader(ticker,'google',start,end)
# 					df.to_csv('stock_dfs/{}.csv'.format(ticker))
# 				except:
# 					continue
# 			else:
# 				print('Already have {}'.format(ticker))
# # get_data_from_yahoo()
def compile_data():
	with open('sp500ticker.pickle','rb') as f:
		tickers = pickle.load(f)
	main_df = pd.DataFrame()
	for count,ticker in enumerate(tickers):
		try:
			print(ticker)
			df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
			# print(df.head())
			df.set_index('Date',inplace=True)
			df.rename(columns = {'Close':ticker}, inplace=True)
			df.drop(['Open','High','Low','Volume'],1,inplace=True)
			print(df.head())
			if main_df.empty:
				main_df = df
			else:
				main_df = main_df.join(df,how='outer')
			if count%10 == 0:
				print(count)
		except:
			continue
	print(main_df.head())
	main_df.to_csv("sp500joined.csv")
# # compile_data()
# def visualise_data():
# 	df = pd.read_csv('sp500joined.csv')
# 	df['AAPL'].plot()
# 	plt.show()
# visualise_data()
compile_data()
