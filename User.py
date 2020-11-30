from ImpConn import *
from Admin import *
from Driver import *
from Message import *

def User():
	global root1
	root1 = Tk()
	root1.geometry('500x500')
	label = Label(root1,text="Welcome To DrivYou",pady=50,font=('courier',30,'bold'))
	label.pack()
	radio1 = Radiobutton(root1,text="Register",value=1,padx=150,font=('courier',15,'bold'),activeforeground='Blue',command = bRegisterU)
	radio1.pack(anchor=W)
	radio2 = Radiobutton(root1,text="Login",value=2,padx=150,font=('courier',15,'bold'),activeforeground='Green',command = bLoginUd)
	radio2.pack(anchor=W)
	radio3 = Radiobutton(root1,text="Exit",value=3,padx=150,font=('courier',15,'bold'),activeforeground='Red',command = root1.destroy)
	radio3.pack(anchor=W)
	root1.mainloop()
	print("Done....")

def RegisterU():
	global root2
	root2 = Tk()
	root2.geometry('500x500')
	Username = StringVar()
	FirstName = StringVar()
	LastName = StringVar()
	Mobile = StringVar()
	Password =StringVar()
	global entry1,entry2,entry3,entry4,entry5
	label = Label(root2,text="Register Here",font=('Helvetica',17,'bold'),pady=5,foreground='blue')
	label.grid(row=0,column=6)
	label1 = Label(root2,text="Username:",font=('Helvetica',17,'bold'),pady=5)
	label1.grid(row=1,column=5)
	label2 = Label(root2,text="FirstName:",font=('Helvetica',17,'bold'),pady=5)
	label2.grid(row=2,column=5)
	label3 = Label(root2,text="LastName:",font=('Helvetica',17,'bold'),pady=5)
	label3.grid(row=3,column=5)
	label4 = Label(root2,text="Mobile:",font=('Helvetica',17,'bold'),pady=5)
	label4.grid(row=4,column=5)
	label5 = Label(root2,text="Password:",font=('Helvetica',17,'bold'),pady=5)
	label5.grid(row=5,column=5)
	entry1 = Entry(root2,relief='flat',font=('Helvetica',12,'italic'))
	entry1.grid(row=1,column=6)
	entry2 = Entry(root2,relief='flat',font=('Helvetica',12,'italic'))
	entry2.grid(row=2,column=6)
	entry3 = Entry(root2,relief='flat',font=('Helvetica',12,'italic'))
	entry3.grid(row=3,column=6)
	entry4 = Entry(root2,relief='flat',font=('Helvetica',12,'italic'))
	entry4.grid(row=4,column=6)
	entry5 = Entry(root2,relief='flat',font=('Helvetica',12,'italic'))
	entry5.grid(row=5,column=6)
	entry5.config(show='*')
	button = Button(root2,text="Submit",padx=10,borderwidth=4,command=InsertU)
	button.grid(row=7,column=3,columnspan=2)
	button2 = Button(root2,text="Login",borderwidth=4,command=bLoginU)
	button2.grid(row=7,column=5,columnspan=2)
	button3 = Button(root2,text="Exit",borderwidth=4,command=root2.destroy)
	button3.grid(row=7,column=7,columnspan=2)

def InsertU():
	Username = str(entry1.get())
	FirstName = str(entry2.get())
	LastName = str(entry3.get())
	Mobile = str(entry4.get())
	Password = str(entry5.get())
	mycursor.execute("SELECT * FROM Customer")
	Result = mycursor.fetchall()
	flag = False
	for x in Result:
		if Username == x[0]:
			print("Username Is Taken....")#print(x)
			flag = True#Register()
			break
	if flag ==True:
		messagebox.showerror("Error","Username Taken..")
		entry1.delete(0,END)
		entry2.delete(0,END)
		entry3.delete(0,END)
		entry4.delete(0,END)
		entry5.delete(0,END)
	if flag == False:
		messagebox.showinfo("Success","Successfully Registered")
		entry1.delete(0,END)
		entry2.delete(0,END)
		entry3.delete(0,END)
		entry4.delete(0,END)
		entry5.delete(0,END)
		sql = """INSERT INTO Customer(Username,FirstName,LastName,Mobile,Password) VALUES (%s, %s, %s, %s, %s)"""
		val = (Username, FirstName, LastName, Mobile, Password)
		mycursor.execute(sql, val)
		mydb.commit()
		print(mycursor.rowcount,"Inserted...")

def LoginU():
	global root3
	root3 = Tk()
	root3.geometry('500x500')
	global entry1,entry2
	label = Label(root3,text="Login Here",foreground='Red',font=('Helvetica',17,'bold','underline'),pady=5)
	label.grid(row=0,column=5)
	label1 = Label(root3,text="Username",font=('Helvetica',17,'bold'),pady=5)
	label1.grid(row=1,column=5)
	label2 = Label(root3,text="Password",font=('Helvetica',17,'bold'),pady=5)
	label2.grid(row=2,column=5)
	entry1 = Entry(root3,relief='flat',font=('Helvetica',12,'italic'))
	entry1.grid(row=1,column=6)
	entry2 = Entry(root3,relief='flat',font=('Helvetica',12,'italic'))
	entry2.grid(row=2,column=6)
	entry2.config(show="*")
	button = Button(root3,text="Submit",borderwidth=4,command=CheckU)
	button.grid(row=3,column=5)
	button1 = Button(root3,text="Back",borderwidth=4,command=backLoginU)
	button1.grid(row=3,column=6)

def CheckU():
	mycursor.execute("SELECT * FROM Customer")
	Result = mycursor.fetchall()
	Username = str(entry1.get())
	Password = str(entry2.get())
	flag = False
	for x in Result:
		if Username == x[0] and Password == x[1]:#print(x)
			flag = True
			break
	if flag == False:
		messagebox.showerror("Error","Username Of Password Not Matched")
		entry1.delete(0,END)
		entry2.delete(0,END)
		print("Username Or Password Not Matched")
	if flag == True:
		bBook()

def Book():
	global root4
	root4 = Tk()
	root4.geometry('500x500')
	label = Label(root4,text="Book Driver Now",padx=50,font=('Helvetica',17,'bold','underline'),foreground='Yellow')
	label.grid(row=1,column=2,columnspan=5)
	global entry1,entry2,entry3,entry4,entry5
	label1 = Label(root4,text="From:",font=('Helvetica',12,'bold'),pady=10)
	label1.grid(row=2,column=1)
	label2 = Label(root4,text="To:",font=('Helvetica',12,'bold'),pady=10)
	label2.grid(row=2,column=3)
	label3 = Label(root4,text="Address:",font=('Helvetica',12,'bold'),pady=10)
	label3.grid(row=3,column=1,columnspan=2)
	label4 = Label(root4,text="Date:",font=('Helvetica',12,'bold'),pady=10)
	label4.grid(row=4,column=1,columnspan=2)
	label5 = Label(root4,text="Mobile:",font=('Helvetica',12,'bold'),pady=10)
	label5.grid(row=5,column=1,columnspan=2)
	entry1 = Entry(root4,relief='flat',font=('Helvetica',12,'italic'))
	entry1.grid(row=2,column=2)
	entry2 = Entry(root4,relief='flat',font=('Helvetica',12,'italic'))
	entry2.grid(row=2,column=4)
	entry3 = Entry(root4,relief='flat',font=('Helvetica',12,'italic'))
	entry3.grid(row=3,column=2,columnspan=3)
	entry4 = Entry(root4,relief='flat',font=('Helvetica',12,'italic'))
	entry4.grid(row=4,column=2,columnspan=3)
	entry5 = Entry(root4,relief='flat',font=('Helvetica',12,'italic'))
	entry5.grid(row=5,column=2,columnspan=3)
	messagebox.showinfo("Information","You're Successfully Logged In...")
	button1 = Button(root4,text="Book",command=Action,borderwidth=4)
	button1.grid(row=6,column=2,columnspan=3)

def Cal(From,To):
	d = distance.distance
	g = Nominatim(user_agent="specify_your_app_name_here",timeout=10)
	_, wa = g.geocode(From)
	_, pa = g.geocode(To)
	return(d(wa, pa).km)

def Fair(Dist):
	if Dist <100:
		return (40+(Dist*2))
	elif Dist >=100 and Dist <500:
		return (100+(Dist*2))
	else:
		return(200+(Dist*4))

def Action():
	global From,To,Address,Date,Mobile
	From = str(entry1.get())
	To = str(entry2.get())
	Address = str(entry3.get())
	Date = str(entry4.get())
	Mobile = str(entry5.get())
	mycursor.execute("SELECT * FROM Driver")
	Result = mycursor.fetchall()
	flag = False
	for x in Result:
		if From == x[5]:
			if x[6] =="No" and x[7] =='Yes':
				root4.destroy()
				global Name
				Name = x[1]
				Messagec("DrivYou",Mobile,x[1],x[2],x[3])
				Messaged("DrivYou",x[3],Address,To,Date)
				Dist = int(Cal(From,To))
				Price = Fair(Dist)
				sql = '''INSERT INTO DrivHist(Username,Distance,Price,Start,End,Date)VALUES(%s,%s,%s,%s,%s,%s)'''
				val = (str(Name),str(Dist),str(Price),str(From),str(To),str(Date))
				mycursor.execute(sql,val)
				mydb.commit()
				Busy = "Yes"
				sql = "UPDATE Driver SET Busy=%s WHERE FirstName=%s"
				val = (Busy,Name)
				mycursor.execute(sql,val)
				mydb.commit()
				print(str(mycursor.rowcount)+"Inserted")
				global root7
				root7 = Tk()
				root7.geometry('500x500')			#New Page....
				label10 = Label(root7,text = "Journey is Booked...journey Details",foreground='Red',font=('Helvetica',17,'bold','underline'))
				label10.grid(row=1,columnspan=4)				#Message One For Driver And For User
				label11 = Label(root7,text = "Name Of Driver:",font=('Helvetica',12,'bold'))
				label11.grid(row=3,columnspan=2)
				label12 = Label(root7,text = x[1],font=('Helvetica',12,'bold'))
				label12.grid(row=3,column=3)
				label13 = Label(root7,text = "Last Name:",font=('Helvetica',12,'bold'))
				label13.grid(row=4,columnspan=2)
				label14 = Label(root7,text = x[2],font=('Helvetica',12,'bold'))
				label14.grid(row=4,column=3)
				label15 = Label(root7,text = "Mobile:",font=('Helvetica',12,'bold'))
				label15.grid(row=5,columnspan=2)
				label21 = Label(root7,text = x[3],font=('Helvetica',12,'bold'))
				label21.grid(row=5,column=3)
				label16 = Label(root7,text = "Distance:",font=('Helvetica',12,'bold'))
				label16.grid(row=6,columnspan=2)
				label17 = Label(root7,text =str(Cal(From,To))+"km",font=('Helvetica',12,'bold'))
				label17.grid(row=6,column=3)
				label18 = Label(root7,text ="Date:",font=('Helvetica',12,'bold'))
				label18.grid(row=7,columnspan=2)
				label20 = Label(root7,text = Date,font=('Helvetica',12,'bold'))
				label20.grid(row=7,column=3)
				label19 = Label(root7,text ="Logout After Complition Of Journey",font=('Helvetica',12,'bold'))
				label19.grid(row=9,columnspan=5)
				button = Button(root7,text="Logout",command=bFeedback,font=('Helvetica',12,'bold'))
				button.grid(row=11)
				flag = True
				break
	if flag == False:
		root4.destroy()
		global root8
		root8 = Tk()
		root8.geometry('500x500')
		messagebox.showerror("Error","Coudn't Locate Any Driver")
		label18 = Label(root8,text="Sorry... No Driver Available In Your City Currently",font=('Dolphin',15,'bold'),foreground='Blue')
		label18.grid(row=1,columnspan=5)
		button4 = Button(root8,text="Logout",borderwidth=4,command=root8.destroy,font=('Helvetica',12,'bold'))
		button4.grid(row=3,column=2)

def Submit():
	messagebox.showinfo("Info","Thank You...Visit Again")
	Behaviour = int(item2.get())
	Time = int(item3.get())
	Recommand = int(item4.get())
	Rules = int(item5.get())
	Overall = int(item6.get())
	mycursor.execute("SELECT * FROM Feedback")
	Result = mycursor.fetchall()
	for x in Result:
		if Name == x[0]:
			New_Behaviour = Behaviour + int(x[1])
			New_Time = Time + int(x[2])
			New_Recommand = Recommand + int(x[3])
			New_Rules = Rules + int(x[4])
			New_Overall = Overall + int(x[5])
			New_Ideal = int(x[6]) + 5
			sql = "UPDATE Feedback SET Behaviour=%s, Time=%s, Recommand=%s, Rules=%s, Overall=%s, Ideal=%s WHERE Name=%s"
			val = (str(New_Behaviour),str(New_Time),str(New_Recommand),str(New_Rules),str(New_Overall),str(New_Ideal),Name)
			mycursor.execute(sql,val)
			mydb.commit()
			Busy = "No"
			sql = "UPDATE Driver SET Busy=%s WHERE FirstName=%s"
			val = (Busy,Name)
			mycursor.execute(sql,val)
			mydb.commit()
			print(mycursor.rowcount, "Record(s) Affected")

def Feedback():
	global root9
	root9 = Tk()
	root9.geometry('700x500')
	global item2,item3,item4,item5,item6
	Behaviour = "How Was The Drivers Behaviour?"
	Time = "Punctuality Of Driver"
	Recommand = "How Much You Will Recommand This Driver?"
	Rules = "Ratings On Traffic Rules"
	Overall = "Overall Experience With Driver"
	messagebox.showerror("Error","Fill Feedback First")
	label1 = Label(root9,text="Feedback",font=('Helvetica',12,'bold','underline'))
	label1.grid(row=1,columnspan=5)
	label2 = Label(root9,text=Behaviour,font=('Helvetica',12,'bold'))
	label2.grid(row=2,columnspan=5)
	item2 = Spinbox(root9,from_=1,to=5,font=('Helvetica',12,'bold'))
	item2.grid(row=3)
	label3 = Label(root9,text=Time,font=('Helvetica',12,'bold'))
	label3.grid(row=4,columnspan=5)
	item3 = Spinbox(root9,from_=1,to=5,font=('Helvetica',12,'bold'))
	item3.grid(row=5)
	label4 = Label(root9,text=Recommand,font=('Helvetica',12,'bold'))
	label4.grid(row=6,columnspan=5)
	item4 = Spinbox(root9,from_=1,to=5,font=('Helvetica',12,'bold'))
	item4.grid(row=7)
	label5 = Label(root9,text=Rules,font=('Helvetica',12,'bold'))
	label5.grid(row=8,columnspan=5)
	item5 = Spinbox(root9,from_=1,to=5,font=('Helvetica',12,'bold'))
	item5.grid(row=9)
	label6 = Label(root9,text=Overall,font=('Helvetica',12,'bold'))
	label6.grid(row=10,columnspan=5)
	item6 = Spinbox(root9,from_=1,to=5,font=('Helvetica',12,'bold'))
	item6.grid(row=11)
	button = Button(root9,text="Submit",command=Submit,font=('Helvetica',12,'bold'))
	button.grid(row=12,column=3)

def bAdmin():
	root.destroy()
	Admin()
def bDetail():
	root11.destroy()
	Detail()
def bDriver(): 			#What Before Selecting Driver
	root.destroy()
	Driver()
def bUser():			#What Before Selecting User
	root.destroy()
	User()
def bRegisterU():		#What Before Selecting Registering User
	root1.destroy()
	RegisterU()
def bLoginU():			#Before Login Inside Registering User
	root2.destroy()
	LoginU()
def bLoginUd():			#Before Login Directly User
	root1.destroy()
	LoginU()
def bBook():			#Before Book
	root3.destroy()
	Book()
def bFeedback():
	root7.destroy()
	Feedback()
def backLoginU():
	root3.destroy()
	RegisterU()

if __name__ == "__main__":
	root = Tk()
	root.geometry('500x500')
	root.title('DrivYou')
	label= Label(root,text="Specify Yourself",pady=50,foreground='Red',font=('TimesNewRoman',30,'bold','underline'))
	label.pack()
	radio1 = Radiobutton(root,text="User",padx=150,state='normal',font=('courier',15,'bold'),command = bUser,activeforeground='Red',value=1)
	radio1.pack(anchor=W)
	radio2 = Radiobutton(root,text="Driver",padx=150,state='normal',font=('courier',15,'bold'),command = bDriver,activeforeground='Blue',value=2)
	radio2.pack(anchor=W)
	radio3 = Radiobutton(root,text="Admin",padx=150,font=('courier',15,'bold'),command = bAdmin,activeforeground='Green',value=3)
	radio3.pack(anchor=W)
	root.mainloop()
