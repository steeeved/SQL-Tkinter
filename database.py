from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Learn to code with Tkinter and sqlite3")
root.iconbitmap("images1.ico")
root.geometry("400x400")


#create database
conn = sqlite3.connect("address_book.db")
c = conn.cursor()

#create a table
'''
c.execute("""CREATE TABLE addresses(
	first_name text,
	last_name text,
	address text,
	city text,
	state text,
	zipcode integer,
	age integer)
	""")
'''
#create submit function
def submit():
	conn = sqlite3.connect("address_book.db")
	c = conn.cursor()
	#Insert to table
	c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :age, :city, :state, :zipcode, :address)", 
			{
				'f_name': f_name.get(),
				'l_name': l_name.get(),
				'age': age.get(),
				'city': city.get(),
				'state': state.get(),
				'zipcode': zipcode.get(),
				'address': address.get()
			})	
	#commit changes
	conn.commit()
	conn.close()
	#Clear textboxes
	f_name.delete(0, END)
	l_name.delete(0, END)
	age.delete(0, END)
	city.delete(0, END)
	state.delete(0, END)
	zipcode.delete(0, END)
	address.delete(0, END)

def query():
	conn = sqlite3.connect("address_book.db")
	c = conn.cursor()
	#Insert to table
	c.execute("SELECT *, oid FROM addresses")
	records = c.fetchall()
	for record in records:
		print(record)
	conn.commit()
	conn.close()


#Create text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
age = Entry(root, width=30)
age.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state= Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)
address= Entry(root, width=30)
address.grid(row=6, column=1, padx=20)

#create textbox lable
f_name_lable = Label(root, text="First Name")
f_name_lable.grid(row=0, column=0)
l_name_lable = Label(root, text="Last Name")
l_name_lable.grid(row=1, column=0)
age_lable = Label(root, text="Age")
age_lable.grid(row=2, column=0)
city_lable = Label(root, text="City")
city_lable.grid(row=3, column=0)
state_lable = Label(root, text="State")
state_lable.grid(row=4, column=0)
zipcode_lable = Label(root, text="Zipcode")
zipcode_lable.grid(row=5, column=0)
address_lable = Label(root, text="Address")
address_lable.grid(row=6, column=0)

#create submit button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Create a query btn
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


#commit changes
conn.commit()
conn.close()


root.mainloop()
