import request_stocks
import json
import pyodbc
import configparser

key = 'UALDBC0E4DVPOVASTA7RSO1M5CIO12S8'
def get_quotes(**kwargs):
	url = 'https://api.tdameritrade.com/v1/marketdata/quotes'

	params = {}
	params.update({'apikey': key})

	symbol_list = []

	for symbol in kwargs.get('symbol'):
		symbol_list.append(symbol)

	params.update({'symbol': symbol_list})
	stock_data = {}
	stock_data = request_stocks.get(url , params = params).json( )

	list_data = [(k,v) for k, v in stock_data['TSLA'].items()]
	print(list_data)
