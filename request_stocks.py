import requests
import json
import pyodbc

class AmeritradeData:
	def __init__(self, key, url):
		self.key = key
		self.symbol_list = []
		self.params = { }
		self.url = url
		self.stock_data = {}
		self.driver = ''

	def get_key(self):
		return self.key

	def get_url(self):
		return self.url

	def get_symbol_list(self,**kwargs):
		list =[]
		for symbol in kwargs.get('companies'):
			list.append(symbol)
		self.symbol_list = list
		return self.symbol_list

	def get_params(self):
		self.params.update({'symbol' : self.symbol_list})
		return self.params

	def get_stock_data(self,url,stock_params):
		stock_data = { }
		stock_data = requests.get(url , params = stock_params).json( )
		print(stock_data)
		return self.stock_data

	def export_data(self):
		with open("stock_data.json", "w") as outfile:
			json.dump(self.stock_data, outfile, indent = 4)
		return print("done")

	def find_driver(self):
		driver_name = ''
		driver_names = [ x for x in pyodbc.drivers( ) if x.endswith(' for SQL Server') ]
		if driver_names:
			driver_name = driver_names[ 0 ]
		if driver_name:
			conn_str = 'DRIVER={}; ...'.format(driver_name)
			self.driver = conn_str
			return self.driver
		else:
			return print('(No suitable driver found. Cannot connect.)')

	def store_data(self):
		sl = self.symbol_list.__iter__()
		sd = self.stock_data
		print(sd)
		#cdb = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=(LocalDB)\\MSSQLLocalDB;Integrated
		# Security=true;')
		#cursor = cdb.cursor()
		for symbol in sl:
			print(symbol)
			list_data = sd.get(symbol).format()
			print(list_data)
			#cursor.execute("INSERT INTO stocks VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (list_data['assetType'],
			# list_data['assetMainType'],list_data['cusip'], list_data['symbol'], list_data['description'], list_data['bidPrice'], list_data['bidSize'], list_data['bidId'], list_data['askPrice'], list_data['openPrice'], list_data['highPrice'], list_data['lowPrice'], list_data['closePrice'], list_data['delayed']))
			#list_data.clear()
			#cursor.execute('SELECT * FROM dbo.stocks')
			#row = cursor.fetchall()
			#print(row)

		#cdb.commit()
		#cursor.close()



