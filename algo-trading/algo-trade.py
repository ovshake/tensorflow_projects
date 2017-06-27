import numpy as np 
import pandas as pd 
import pickle 
from collections import Counter

def process_data_for_labels(ticker):
	hm_days = 7
	df = pd.read_csv('sp500joined.csv')
	tickers = df.columns.values.tolist()
	df.fillna(0,inplace=True)
	# print(df.head())
	for i in range(1,hm_days+1):
		df['{}_{}d'.format(ticker,i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]
	df.fillna(0,inplace=True)
	return tickers,df

def buy_sell_hold(*args):
	cols = [c for c in args]
	required = 0.02
	for col in cols:
		if(col > required):
			return 1
		if(col < -required):
			return -1
	return 0

def extract_featuresets(ticker):
	tickers,df = process_data_for_labels(ticker)
	df['{}_target'.format(ticker)] = list(map(buy_sell_hold, df['{}_1d'.format(ticker)],
																df['{}_2d'.format(ticker)],
																df['{}_3d'.format(ticker)],
																df['{}_4d'.format(ticker)],
																df['{}_5d'.format(ticker)],
																df['{}_6d'.format(ticker)],
																df['{}_7d'.format(ticker)],
																 ))
	vals = df['{}_target'.format(ticker)].values.tolist()
	str_vals = [str(i) for i in vals]
	print('Data Spread',Counter(str_vals))
	df.fillna(0,inplace=True)
	df = df.replace([np.inf, -np.inf],np.nan)
	df.dropna(inplace=True)
	df_vals = df[[ticke for ticke in tickers]].pct_change()
	df_vals = df_vals.replace([np.inf, -np.inf],0)
	df_vals.fillna(0,inplace=True)
	X = df_vals.values.tolist()
	y = df['{}_target'.format(ticker)].values
	return X,y,df
extract_featuresets('XOM')
print("asds")