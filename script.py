import request_stocks as rs



if __name__ == "__main__":
	key = 'UALDBC0E4DVPOVASTA7RSO1M5CIO12S8'
	url = 'https://api.tdameritrade.com/v1/marketdata/quotes'
	stock = rs.AmeritradeData(key, url)
	stock_data = {}
	stock_data = requests.get(url, params=)
	symbol_list= stock.get_symbol_list(companies = [ 'TSLA' , 'BNDSF' , 'AEGOF' , 'RAZFF' , 'DUFRY' ])

	print("\nKEY: "+stock.get_key() +"\nURL: " + stock.get_url() +"\nsymbol_list: ")
	for x in symbol_list:
		print(x)


	# companies = stock.get_companies(symbol= ['TSLA', 'BNDSF','AEGOF','RAZFF','DUFRY'])
	stock_params = stock.get_params()
	stock.find_driver()
	stock_data = stock.get_stock_data(url, stock_params)
	stock.store_data()

