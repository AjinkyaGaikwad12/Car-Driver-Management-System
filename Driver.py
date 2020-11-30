from ImpConn import *
from User import *

def backLoginD():
	root3.destroy()
	RegisterD()
def bDpage():
	root3.destroy()
	Dpage()
def bRegisterD():		#What Before Selecting Registering Driver
	root5.destroy()
	RegisterD()
def bLoginD():			#Before Login Inside Registering Driver
	root6.destroy()
	LoginD()
def bLoginDd():			#Before Login Directly Driver
	root5.destroy()
	LoginD()

def Driver():
	global root5
	root5 = Tk()
	root5.geometry('500x500')
	label = Label(root5,text="Welcome To DrivYou",pady=50,font=('courier','30','bold'))
	label.pack()
	radio1 = Radiobutton(root5,text="Register",value=1,padx=150,font=('courier','15','bold'),activeforeground='Blue',command = bRegisterD)
	radio1.pack(anchor=W)
	radio2 = Radiobutton(root5,text="Login",value=2,padx=150,font=('courier','15','bold'),activeforeground='Green',command = bLoginDd)
	radio2.pack(anchor=W)
	radio3 = Radiobutton(root5,text="Exit",value=3,padx=150,font=('courier','15','bold'),activeforeground='Red',command = root5.destroy)
	radio3.pack(anchor=W)
	root5.mainloop()

def RegisterD():
	global root6
	root6 = Tk()
	root6.geometry('500x500')
	Username = StringVar()
	FirstName = StringVar()
	LastName = StringVar()
	Mobile = StringVar()
	Password = StringVar()
	Location = StringVar()
	global entry1,entry2,entry3,entry4,entry5
	global entry6
	label = Label(root6,text="Register Here",font=('Helvetica',17,'bold'),pady=5,foreground='blue')
	label.grid(row=0,column=6)
	label1 = Label(root6,text="Username:",font=('Helvetica',17,'bold'),pady=5)
	label1.grid(row=1,column=5)
	label2 = Label(root6,text="FirstName:",font=('Helvetica',17,'bold'),pady=5)
	label2.grid(row=2,column=5)
	label3 = Label(root6,text="LastName:",font=('Helvetica',17,'bold'),pady=5)
	label3.grid(row=3,column=5)
	label4 = Label(root6,text="Mobile:",font=('Helvetica',17,'bold'),pady=5)
	label4.grid(row=4,column=5)
	label5 = Label(root6,text="Password:",font=('Helvetica',17,'bold'),pady=5)
	label5.grid(row=5,column=5)
	label6 = Label(root6,text="Location:",font=('Helvetica',17,'bold'),pady=5)
	label6.grid(row=6,column=5)
	entry1 = Entry(root6,relief='flat',font=('Helvetica',12,'italic'))
	entry1.grid(row=1,column=6)
	entry2 = Entry(root6,relief='flat',font=('Helvetica',12,'italic'))
	entry2.grid(row=2,column=6)
	entry3 = Entry(root6,relief='flat',font=('Helvetica',12,'italic'))
	entry3.grid(row=3,column=6)
	entry4 = Entry(root6,relief='flat',font=('Helvetica',12,'italic'))
	entry4.grid(row=4,column=6)
	entry5 = Entry(root6,relief='flat',font=('Helvetica',12,'italic'))
	entry5.grid(row=5,column=6)
	entry5.config(show='*')
	entry6 = Entry(root6,relief='flat',font=('Helvetica',12,'italic'))
	entry6.grid(row=6,column=6)
	button = Button(root6,text="Submit",padx=10,borderwidth=4,command=InsertD)
	button.grid(row=7,column=3,columnspan=2)
	button2 = Button(root6,text="Login",borderwidth=4,command=bLoginD)
	button2.grid(row=7,column=5,columnspan=2)
	button3 = Button(root6,text="Exit",borderwidth=4,command=root6.destroy)
	button3.grid(row=7,column=7,columnspan=2)

def InsertD():
	Username = str(entry1.get())
	FirstName = str(entry2.get())
	LastName = str(entry3.get())
	Mobile = str(entry4.get())
	Password = str(entry5.get())
	Location = str(entry6.get())
	Busy = "No"
	Validate = "No"
	mycursor.execute("SELECT * FROM Driver")
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
		entry6.delete(0,END)
	if flag == False:
		messagebox.showinfo("Success","Successfully Registered")
		entry1.delete(0,END)
		entry2.delete(0,END)
		entry3.delete(0,END)
		entry4.delete(0,END)
		entry5.delete(0,END)
		entry6.delete(0,END)
		sql = """INSERT INTO Driver(Username,FirstName,LastName,Mobile,Password,Location,Busy,Validate) VALUES (%s,%s, %s, %s, %s, %s, %s, %s)"""
		val = (Username, FirstName, LastName, Mobile, Password, Location, Busy, Validate)
		mycursor.execute(sql, val)
		mydb.commit()
		Behaviour = 0
		Time = 0
		Recommand = 0
		Rules = 0
		Overall = 0
		Ideal = 0
		sql = """INSERT INTO Feedback(Name,Behaviour,Time,Recommand,Rules,Overall,Ideal) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
		val = (FirstName, Behaviour, Time, Recommand, Rules, Overall, Ideal)
		mycursor.execute(sql, val)
		mydb.commit()
		print(mycursor.rowcount,"Inserted...")

def LoginD():
	global root3
	root3 = Tk()
	root3.geometry('500x500')
	global entry1,entry2
	label = Label(root3,text="Login Here",foreground='Red',font=('Helvetica',17,'bold','underline'),pady=5)
	label.grid(row=0,column=5,columnspan=5)
	label1 = Label(root3,text="Username",font=('Helvetica',17,'bold'),pady=5)
	label1.grid(row=1,column=5)
	label2 = Label(root3,text="Password",font=('Helvetica',17,'bold'),pady=5)
	label2.grid(row=2,column=5)
	entry1 = Entry(root3,relief='flat',font=('Helvetica',12,'italic'))
	entry1.grid(row=1,column=6)
	entry2 = Entry(root3,relief='flat',font=('Helvetica',12,'italic'))
	entry2.grid(row=2,column=6)
	entry2.config(show="*")
	button = Button(root3,text="Submit",borderwidth=4,command=CheckD)
	button.grid(row=3,column=5)
	button1 = Button(root3,text="Back",borderwidth=4,command=backLoginD)
	button1.grid(row=3,column=6)

def CheckD():
	mycursor.execute("SELECT * FROM Driver")
	Result = mycursor.fetchall()
	global Username,Namu
	Username = str(entry1.get())
	Password = str(entry2.get())
	print(Username)
	flag = False
	for x in Result:
		if Username == x[0] and Password == x[4]:#print(x)
			flag = True
			Namu = x[1]
			break
	if flag == False:
		messagebox.showerror("Error","Username Of Password Not Matched")
		entry1.delete(0,END)
		entry2.delete(0,END)
		print("Username Or Password Not Matched")
	if flag == True:
		bDpage()

def Dpage():
	global root14
	root14 = Tk()
	root14.geometry('500x500')
	messagebox.showinfo("Success","Welcome "+ Username)
	label = Label(root14,text="Trips Details",font=('Helvetica',17,'bold','underline'),foreground='Red')
	label.grid(row=1,column=4)
	mycursor.execute("SELECT * FROM DrivHist")
	Result = mycursor.fetchall()
	#print(Result)
	flagname = False
	for y in Result:
		if y[0] == Namu:
			flagname = True
	if flagname:
		i = 2
		for x in Result:
			if x[0] == Namu:
				label1 = Label(root14,text="Start:",font=('Helvetica',12,'bold'),pady=5)
				label1.grid(row=2,column=i)
				label2 = Label(root14,text=x[3],font=('Helvetica',12,'bold'),pady=5)
				label2.grid(row=2,column=i+1)
				label3 = Label(root14,text="End:",font=('Helvetica',12,'bold'),pady=5)
				label3.grid(row=3,column=i)
				label4 = Label(root14,text=x[4],font=('Helvetica',12,'bold'),pady=5)
				label4.grid(row=3,column=i+1)
				label5 = Label(root14,text="Date:",font=('Helvetica',12,'bold'),pady=5)
				label5.grid(row=4,column=i)
				label6 = Label(root14,text=x[5],font=('Helvetica',12,'bold'),pady=5)
				label6.grid(row=4,column=i+1)
				label7 = Label(root14,text="Distance:",font=('Helvetica',12,'bold'),pady=5)
				label7.grid(row=5,column=i)
				label8 = Label(root14,text=x[1],font=('Helvetica',12,'bold'),pady=5)
				label8.grid(row=5,column=i+1)
				label9 = Label(root14,text="Price:",font=('Helvetica',12,'bold'),pady=5)
				label9.grid(row=6,column=i)
				label10 = Label(root14,text=x[2],font=('Helvetica',12,'bold'),pady=5)
				label10.grid(row=6,column=i+1)
				i = i + 2
	else:
		label = Label(root14,text="No Trips Done Yet...",font=('Helvetica',15,'italic'),pady=5,foreground='Yellow')
		label.grid(row=4,columnspan=5)
	label = Label(root14,text="Add Additional Information",font=('Helvetica',17,'bold','underline'),pady=5,foreground='Red')
	label.grid(row=8,columnspan=5)
	button = Button(root14,text='Click Here',borderwidth=4,command=Addinfo)
	button.grid(row=9,columnspan=4)

def Addinfo():
	root14.destroy()
	global root15
	root15 = Tk()
	root15.geometry('500x500')
	global entry1,entry2,entry3,entry4
	label = Label(root15,text="Details",padx=100,font=('Helvetica',17,'bold','underline'),pady=5,foreground='Green')
	label.grid(row=1,column=1,columnspan=5)
	label1 = Label(root15,text="Adhar:",font=('Helvetica',12,'bold'),pady=5)
	label1.grid(row=2,column=1)
	label2 = Label(root15,text="License:",font=('Helvetica',12,'bold'),pady=5)
	label2.grid(row=3,column=1)
	label3 = Label(root15,text="Age:",font=('Helvetica',12,'bold'),pady=5)
	label3.grid(row=4,column=1)
	label4 = Label(root15,text="Experience:",font=('Helvetica',12,'bold'),pady=5)
	label4.grid(row=5,column=1)
	entry1 = Entry(root15,relief='flat',font=('Helvetica',12,'italic'))
	entry1.grid(row=2,column=2)
	entry2 = Entry(root15,relief='flat',font=('Helvetica',12,'italic'))
	entry2.grid(row=3,column=2)
	entry3 = Entry(root15,relief='flat',font=('Helvetica',12,'italic'))
	entry3.grid(row=4,column=2)
	entry4 = Entry(root15,relief='flat',font=('Helvetica',12,'italic'))
	entry4.grid(row=5,column=2)
	button = Button(root15,text="Submit",borderwidth=4,command=Finalsub)
	button.grid(row=6,columnspan=4)

def Finalsub():
	print(Namu)
	flag = False
	Adhar = str(entry1.get())
	License = str(entry2.get())
	Age = str(entry3.get())
	Experience = str(entry4.get())
	sql = "INSERT INTO Details(Adhar,License,Age,Experience,Name) VALUES(%s,%s,%s,%s,%s)"
	val = (Adhar,License,Age,Experience,Namu)
	mycursor.execute(sql,val)
	mydb.commit()
	if mycursor.rowcount:
		flag = True
	print(str(mycursor.rowcount)+" Inserted")
	if flag == True:
		sql = "UPDATE Driver SET Validate = %s where FirstName = %s"
		val = ('Yes',Namu)
		mycursor.execute(sql,val)
		mydb.commit()
		print(mycursor.rowcount,"Inserted")
		entry1.delete(0,END)
		entry2.delete(0,END)
		entry3.delete(0,END)
		entry4.delete(0,END)
