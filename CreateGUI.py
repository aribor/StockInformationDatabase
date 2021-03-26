import datarequest as dr
import sqlite3 as sql
from tkinter.filedialog import *
from tkinter import messagebox as mb

class DatabaseGui:
	def __init__(self, master): #master is root
		mainFrame = Frame(master)
		self.master = master

		master.title("Ameritrade Database GUI")
		# global x_pos, y_pos
		self.w = 500  # width for the Tk root
		self.h = 340  # height for the Tk root
		#
		# # get screen width and height
		self.ws = master.winfo_screenwidth( )  # width of the screen
		self.hs = master.winfo_screenheight( )  # height of the screen
		#
		#
		#
		# # calculate x and y coordinates for the Tk root window
		self.x = (self.ws / 2) - (self.w / 2)
		self.y = (self.hs / 2) - (self.h / 2)
		#
		# # set the dimensions of the screen and where it is placed
		root.geometry('%dx%d+%d+%d' % (self.w , self.h , self.x , self.y))
		mainFrame.pack()

		# Custom Ameritrade Image for Master Page
		img = PhotoImage(file = "Images/td_ameritradeLOGO.png")

		img_label = Label(master , image = img, pady=20)
		img_label.image = img
		img_label.pack(side=TOP)
		# MASTER PAGE QUIT AND SEARCH BUTTONS
		self.quit_button = Button(master, text = "Quit", command=master.quit)
		self.quit_button.pack(side=BOTTOM, fill=X,ipady=30)
		self.search_button = Button(master , text = "Search Company Database" , command = self.search)
		self.search_button.pack(side = BOTTOM , fill = X , ipady = 30)


	def search(self):
		#series of search-focused functions
		# after selecting "search company database" button, the user has the option to:
		# export the current table
		# search for companies
		# display the current table (show stocks)
		# Dropping the table
		# creating a new table
		def save():
			cdb = sql.connect('stock_data.db')
			cursor = cdb.cursor( )

			files = [ ('All Files' , '*.*') ,
			          ('Text Document' , '*.txt') ,
			          ('CSV (Comma delimited)' , "*.csv") ,
			          ('JSON' , '*.json') ]
			cursor.execute("SELECT * FROM stocks")
			stock_data = cursor.fetchall( )
			#print(stock_data)
			filename = asksaveasfilename(filetypes = files , defaultextension = files)
			dr.export_data( filename, stock_data)
		def search_company():
			# list created to store company names upon user entry
			comp_name = []
			comp_name.append(company_entry.get())
			dr.get_quotes(symbol= comp_name)
			mb.showinfo(title="Database Info", message = 'Database was created successfully!')
			company_entry.delete(0,END)


		def show_stocks():
			# new Toplevel window created for the user to see the table stored in the database
			cdb = sql.connect('stock_data.db')
			cursor = cdb.cursor( )
			database = Toplevel()
			database.title("Database View")
			try:
				cursor.execute("SELECT * FROM stocks")
			except sql.Error as er:
				mb.showerror(title="database error", message='SQLite error: %s' % (' '.join(er.args)))
			i = 1
			# loop through stock data results
			# ADD table headers
			col0 = Entry(database, width =10, fg = 'black')
			col0.grid(row = 0, column = 0)
			col0.insert(0, "[assetType]")
			col1 = Entry(database , width = 10 , fg = 'black')
			col1.grid(row = 0 , column = 1)
			col1.insert(0, "[assetMainType]")
			col2 = Entry(database , width = 10 , fg = 'black')
			col2.grid(row = 0 , column = 2)
			col2.insert(0 , "[cusip]")
			col3 = Entry(database , width = 10 , fg = 'black')
			col3.grid(row = 0 , column = 3)
			col3.insert(0, "[symbol]")
			col4 = Entry(database , width = 10 , fg = 'black')
			col4.grid(row = 0 , column = 4)
			col4.insert(0 , "[description]")
			col5 = Entry(database , width = 10 , fg = 'black')
			col5.grid(row = 0 , column = 5)
			col5.insert(0 , "[bidPrice]")
			col6 = Entry(database , width = 10 , fg = 'black')
			col6.grid(row = 0 , column = 6)
			col6.insert(0 , "[bidSize]")
			col7 = Entry(database , width = 10 , fg = 'black')
			col7.grid(row = 0 , column = 7)
			col7.insert(0 , "[bidId]")
			col8 = Entry(database , width = 10 , fg = 'black')
			col8.grid(row = 0 , column = 8)
			col8.insert(0 , "[askPrice]")
			col9 = Entry(database , width = 10 , fg = 'black')
			col9.grid(row = 0 , column = 9)
			col9.insert(0 , "[openPrice]")
			col10 = Entry(database , width = 10 , fg = 'black')
			col10.grid(row = 0 , column = 10)
			col10.insert(0 , "[highPrice]")
			col11 = Entry(database , width = 10 , fg = 'black')
			col11.grid(row = 0 , column = 11)
			col11.insert(0 , "[lowPrice]")
			col12 = Entry(database , width = 10 , fg = 'black')
			col12.grid(row = 0 , column = 12)
			col12.insert(0 , "[closePrice]")
			col13 = Entry(database , width = 10 , fg = 'black')
			col13.grid(row = 0 , column = 13)
			col13.insert(0 , "[delayed]")
			# add their data to entries entries
			for rows in cursor:
				for columns in range(len(rows)):
					print_info = Entry(database, width = 10, fg ='blue')
					print_info.grid(row = i+1, column = columns)
					print_info.insert(END, rows[columns])
				i = i+1
			# clear_btn = Button(database , text = "Delete Table" , command = clear())
			# clear_btn.grid(row = i + 3 , column = 1 , columnspan = 2 , pady = 10 , padx = 10 , ipadx = 100)
			export_button = Button(database, text= "Export Data", command=lambda : save())
			export_button.grid(row =i+1, columnspan=14,ipady=20,sticky='NESW' )
			quit_database = Button(database, text = "Quit", command = database.quit)
			quit_database.grid(row = i+2, columnspan =14,ipady=20,sticky='NESW')
		def drop_table():
			#dropping the table uses the "delete_table" datarequest.py function
			#returns a message upon success
			dr.delete_table()
			mb.showinfo(title="Database Info", message="Table has been dropped.")
		def new_table():
			# dropping the table uses the "delete_table" and "new_table"
			# datarequest.py functions
			# this eliminated problems where a table already existed
			# therefore, each time a user asks for a new table the previous
			# table will always be deleted returns a message upon success
			dr.delete_table()
			dr.create_table()
			mb.showinfo(title = "Database Info" , message = "A new table has been successfully created.")
		# search page is a toplevel version of the master (or parent) window.
		search = Toplevel()
		search.title("Search Database")

		#entry where the user types the company name
		company_entry = Entry(search, text="search company here", fg='grey')
		company_entry.grid(row=1, column=1,pady=20,padx=10,sticky='NESW')

		comp_label = Label(search, text = "Symbol")
		comp_label.grid(row =1, column=0, ipadx= 10,ipady=20, sticky='NESW')
		# series of buttons created (search company, Quit, Show Stocks, Export, Drop table,
		# and new table
		submit_btn = Button(search, text="Search",pady=20,command=search_company)
		submit_btn.grid(row=2, column=0,columnspan = 2,sticky='NESW')
		search_quit = Button(search, text = "Quit", command=search.quit)
		search_quit.grid(row=6,columnspan=2,sticky='NESW')

		query_btn = Button(search, text = "Show Stock Data", command =show_stocks)
		query_btn.grid(row=3,column=0,sticky='NESW')
		export_search = Button(search, text = "Export database",command= lambda :save())
		export_search.grid(row=3,column=1,sticky='NESW')
		drop_stock = Button(search, text="Drop Table",command = drop_table)
		drop_stock.grid(row=4,columnspan=2,sticky='NESW')
		new_table_btn = Button(search, text = "New Table", command= new_table)
		new_table_btn.grid(row=5,columnspan=2,sticky='NESW')



#script to run the program

root = Tk() # create a Tk root window
my_gui = DatabaseGui(root)
root.mainloop()
