import request_stocks
import json
import pyodbc
import configparser
key = 'KO66jJmyOksNKk3Wef5Ysq8vz'


def get_quotes(**kwargs):
	url = 'https://api.twitch.tv/helix/streams'

	params = {}
	params.update({'tweet.fields': created_at, 'expansions':author_id, 'user.fields':includes.users.created_at})

	symbol_list = []

	for symbol in kwargs.get('symbol'):
		symbol_list.append(symbol)

	params.update({'symbol': symbol_list})
	stock_data = {}
	stock_data = request_stocks.get(url , params = params).json( )
	# for x in stock_data.values():
	# 	print(x)
	# 	for y in x.values():
	# 		print(y)
	export_data(stock_data)



def export_data(stock_data):
	with open("data.json", "w") as outfile:
		json_str = json.dumps(stock_data)
		json.dump(stock_data, outfile, indent = 4)
	resp = json.loads(json_str)
	# for x in resp['TSLA']:
	# 	print(x)
	# print(resp['TSLA']['assetType'])

	# configFeed = configparser.configParser()
	# configFeed.read('')
	# pymysql = pyodbc.connect('470-project.mdf')
	# cursor = pymysql.cursor()
	# cursor.execute("INSERT INTO stocks VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", resp[s]['assetType'], (resp[s]['assetMainType'],resp[s]['cusip'], resp[s]['symbol'],resp[s]['description'], resp[s]['bidPrice'], resp[s]['askPrice'], resp[s]['openPrice'], resp[s]['highPrice'], resp[s]['lowPrice'], resp[s]['closePrice'], resp[s]['delayed']))


get_quotes(symbol = ['TSLA'])
