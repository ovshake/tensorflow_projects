import numpy as np 
import pandas as pd 
import pickle 

def process_data_for_labels(ticker):
	hm_days = 7
	df = pd.read_csv('sp500joined.csv')
	tickers = df.columns.values.tolist()
	df.fillna(0,inplace=True)
	print(df.head())
	for i in range(1,hm_days+1):
		df['{}_{}d'.format(ticker,i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]
	df.fillna(0,inplace=True)
	return tickers,df

process_data_for_labels('XOM') 
print("dsa")