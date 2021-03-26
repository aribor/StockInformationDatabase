import requests
import json
import sqlite3

# get apikey from config
from config import API_KEY, API_URL
import csv

#main function that requests the stock information
def get_quotes( **kwargs):


	params = {}
	params.update({'apikey': API_KEY})

	symbol_list = []

	for symbol in kwargs.get('symbol'):
		symbol_list.append(symbol)

	params.update({'symbol': symbol_list})
	# stock_data is a dictionary where the requested data is stored into
	stock_data = {}
	stock_data = requests.get(API_URL , params = params).json()
	# data is then automatically added to the database by passing the stock_data
	# and symbol_list (the list of company names)
	add_data(stock_data,symbol_list)
def export_data( filename, stock_data):
	#this function is to assist in the frontend's "export_data" feature
	with open(filename, "w") as outfile:
		json.dump(stock_data, outfile, indent = 4)
		outfile.close()


#table is created and database is created. The database is temporary and only exists before
# relaunching application and "searching company database"
def create_table():
	cdb = sqlite3.connect('stock_data.db')
	cursor = cdb.cursor( )
	cursor.execute('''CREATE TABLE stocks (
	    [assetType]          VARCHAR (30) NULL,
	    [assetMainType]   VARCHAR (30) NULL,
	    [cusip]           VARCHAR (30) NULL,
	    [symbol]          VARCHAR (30) NULL,
	    [description]     VARCHAR (80) NULL,
	    [bidPrice]        VARCHAR (30) NULL,
	    [bidSize]         VARCHAR (30) NULL,
	    [bidId]           VARCHAR (30) NULL,
	    [askPrice]        VARCHAR (30) NULL,
	    [openPrice]       VARCHAR (30) NULL,
	    [highPrice]       VARCHAR (30) NULL,
	    [lowPrice]        VARCHAR (30) NULL,
	    [closePrice]      VARCHAR (30) NULL,
		[delayed]		  VARCHAR (30) NULL
	);''')
	cdb.commit()
	cursor.close()
	#adding requested data to the database
def add_data(stock_data, symbol_list):
	cdb = sqlite3.connect('stock_data.db')
	cursor = cdb.cursor( )
	#exceptions handled if the table is not created.
	try:
		for symbol in symbol_list:
			# Using a list allowed for dynamic insertions to the database
			list_data = [ ]
			list_data = stock_data.get(symbol)
			cursor.execute("INSERT INTO stocks VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)" ,
			            (list_data[ 'assetType' ] , list_data[
				               'assetMainType' ] , list_data[ 'cusip' ] , list_data[ 'symbol' ] ,
			                list_data[ 'description' ] , list_data[ 'bidPrice' ] , list_data[ 'bidSize' ] ,
			                list_data[ 'bidId' ] , list_data[ 'askPrice' ] , list_data[ 'openPrice' ] ,
			                list_data[ 'highPrice' ] , list_data[ 'lowPrice' ] , list_data[ 'closePrice' ] ,
			                list_data[ 'delayed' ]))
	except sqlite3.Error as er:
		return 'SQLite error: %s' % (' '.join(er.args))
	cdb.commit()
	cursor.close()
	return 'Success'
# table is deleted when user requests it
def delete_table():
	cdb = sqlite3.connect('stock_data.db')
	cursor = cdb.cursor( )
	cursor.execute("DROP TABLE if exists stocks")
	cdb.commit()
	cursor.close()
# displaying stocks for the user.
def display_stocks():
	conn = sqlite3.connect('stock_data.db')
	c = conn.cursor()
	c.execute("SELECT *, oid FROM stocks")
	rows = c.fetchall( )
	return rows


#get_quotes(symbol = [ 'TSLA' , 'BNDSF' , 'AEGOF' , 'RAZFF' , 'DUFRY' ])

# THIS WAS A PAST SOLUTION FOR FINDING AN ODBC DRIVER FOR THE PROGRAM TO USE.
# THIS FUNCTION IS MORE PERSONALIZED FOR ADVANCED DATABASE USERS AND PROGRAMMERS
# def find_driver():
# 	driver_name = ''
#
# 	driver_names = [x for x in pyodbc.drivers() if x.endswith(' for SQL Server')]
#
# 	if driver_names:
# 		driver_name = driver_names[ 0 ]
#
# 	if driver_name:
#
# 		conn_str = 'DRIVER={}; ...'.format(driver_name)
#
# 		print(conn_str)
#
# 	else:
#
# 		print('(No suitable driver found. Cannot connect.)')
