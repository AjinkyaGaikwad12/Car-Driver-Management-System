from ImpConn import *
from User import *

def Admin():
	global root10
	root10 = Tk()
	root10.geometry('500x500')
	global entry1,entry2
	label = Label(root10,text="Administartion Login",pady=50,padx=50,foreground='Green',font=('TimesNewRoman',30,'bold','underline'))
	label.grid(row=1,columnspan=10)
	label1 = Label(root10,text="Username:",pady=15,foreground='Blue',font=('Helvetica',15,'bold','italic'))
	label1.grid(row=2)
	entry1 = Entry(root10,font=('courier',10,'italic'),relief='flat')
	entry1.grid(row=2,column=2)
	label2 = Label(root10,text="Password:",pady=15,foreground='Blue',font=('Helvetica',15,'bold','italic'))
	label2.grid(row=3)
	entry2 = Entry(root10,font=('courier',10,'italic'),relief='flat')
	entry2.grid(row=3,column=2)
	entry2.config(show="*")
	button = Button(root10,padx=100,pady=10,text="Submit",font=('Helvetica',10,'bold'),command=CheckA)
	button.grid(row=4,columnspan=10)

def CheckA():
	Username = str(entry1.get())
	Password = str(entry2.get())
	if Username == "Rahul" and Password == "Rahul007":
		root10.destroy()
		global root11
		root11 = Tk()
		root11.geometry('500x500')
		mycursor.execute("SELECT * FROM Driver")
		Result = mycursor.fetchall()
		i = 1
		j = 0
		count = 0
		for x in Result:
			count = count + 1
			if i == 5:
				j = j + 5
				i = 1
			label1 = Label(root11,pady=20,text="Driver Number: "+str(count),font=('courier',10,'italic'))
			label1.grid(row=4+j,column=i)
			label4 = Label(root11,pady=20,text="Name:",font=('courier',10,'italic'))
			label4.grid(row=6+j,column=i)
			label5 = Label(root11,pady=20,text="Mobile:",font=('courier',10,'italic'))
			label5.grid(row=7+j,column=i)
			label6 = Label(root11,pady=20,text="Location:",font=('courier',10,'italic'))
			label6.grid(row=8+j,column=i)
			label7 = Label(root11,pady=20,text="Username:",font=('courier',10,'italic'))
			label7.grid(row=5+j,column=i)
			label8 = Label(root11,pady=20,text=x[0],font=('courier',10,'italic'))
			label8.grid(row=5+j,column=i+1)
			label9 = Label(root11,pady=20,text=x[1],font=('courier',10,'italic'))
			label9.grid(row=6+j,column=i+1)
			label10 = Label(root11,pady=20,text=x[3],font=('courier',10,'italic'))
			label10.grid(row=7+j,column=i+1)
			label2 = Label(root11,pady=20,text=x[5],font=('courier',10,'italic'))
			label2.grid(row=8+j,column=i+1)
			i = i + 2
		messagebox.showinfo("Welcome","Welcome Rahul")
		label3 = Label(root11,pady=20,text="Enter Name Of Driver",font=('courier',15,'bold'))
		label3.grid(row=1,column=1)
		global entry3
		entry3 = Entry(root11,font=('courier',15,'italic'),relief='flat')
		entry3.grid(row=2,column=1)
		button2 = Button(root11,pady=10,text="Select",font=('Helvetica',10,'bold'),command=Detail)
		button2.grid(row=3,column=1)
	else:
		messagebox.showerror("Error","Invalid Admin")
		entry1.delete(0,END)
		entry2.delete(0,END)

def Detail():
	global root12
	root12 = Tk()
	root12.geometry('500x500')
	dist = 0
	price = 0
	count = 0
	Naav = str(entry3.get())
	print(Naav)
	print("Aj")
	root11.destroy()
	label = Label(root12,text="Driver Details",pady=10,font=('Helvetica',15,'italic','underline','bold'))
	label.grid(row=1,column=1,columnspan=2)
	mycursor.execute("SELECT * FROM Driver")
	Result_driver = mycursor.fetchall()
	mycursor.execute("SELECT * FROM DrivHist")
	Result_hist = mycursor.fetchall()
	mycursor.execute("SELECT * FROM Feedback")
	Result = mycursor.fetchall()
	for z in Result_driver:
		if Naav == z[1]:
			surname = z[2]
			mobile = z[3]
			Home = z[5]
	for y in Result_hist:
		if Naav == y[0]:
			dist = dist + int(y[1])
			price = price + int(y[2])
			count = count + 1
	for x in Result:
		if Naav == x[0]:
			Max = int(x[6])
			div = Max/5
			Behav = (int(x[1])/div)
			Tim = (int(x[2])/div)
			Recom = (int(x[3])/div)
			Rul = (int(x[4])/div)
			Over = float(Behav+Tim+Recom+Rul)/4
			Max = (int(x[6])/div)
	label8 = Label(root12,text="Name:",pady=10,font=('Helvetica',15,'bold'))
	label8.grid(row=2,column=1)
	label1 = Label(root12,text=Naav,pady=10,font=('Helvetica',15,'bold'))#print("yo")
	label1.grid(row=2,column=2)
	label6 = Label(root12,text="Surname:",pady=10,font=('Helvetica',15,'bold'))
	label6.grid(row=3,column=1)
	label2 = Label(root12,text=surname,pady=10,font=('Helvetica',15,'bold'))
	label2.grid(row=3,column=2)
	label9 = Label(root12,text="Total Distance:",pady=10,font=('Helvetica',15,'bold'))
	label9.grid(row=4,column=1)
	label3 = Label(root12,text=dist,pady=10,font=('Helvetica',15,'bold'))
	label3.grid(row=4,column=2)
	label10 = Label(root12,text="Total Fare:",pady=10,font=('Helvetica',15,'bold'))
	label10.grid(row=5,column=1)
	label4 = Label(root12,text=price,pady=10,font=('Helvetica',15,'bold'))
	label4.grid(row=5,column=2)
	label7 = Label(root12,text="Home City:",pady=10,font=('Helvetica',15,'bold'))
	label7.grid(row=6,column=1)
	label5 = Label(root12,text=Home,pady=10,font=('Helvetica',15,'bold'))
	label5.grid(row=6,column=2)
	label0 = Label(root12,text=" Feedback Recieved",pady=10,font=('Helvetica',15,'italic','underline','bold'))
	label0.grid(row=1,column=5)
	label11 = Label(root12,text="Behaviour:",pady=10,font=('Helvetica',15,'bold'))
	label11.grid(row=2,column=5)
	label12 = Label(root12,text=Behav,pady=10,font=('Helvetica',15,'bold'))
	label12.grid(row=2,column=6)
	label13 = Label(root12,text="Time Manage:",pady=10,font=('Helvetica',15,'bold'))
	label13.grid(row=3,column=5)
	label14 = Label(root12,text=Tim,pady=10,font=('Helvetica',15,'bold'))
	label14.grid(row=3,column=6)
	label15 = Label(root12,text="Recommandation:",pady=10,font=('Helvetica',15,'bold'))
	label15.grid(row=4,column=5)
	label16 = Label(root12,text=Recom,pady=10,font=('Helvetica',15,'bold'))
	label16.grid(row=4,column=6)
	label17 = Label(root12,text="Rules:",pady=10,font=('Helvetica',15,'bold'))
	label17.grid(row=5,column=5)
	label18 = Label(root12,text=Rul,pady=10,font=('Helvetica',15,'bold'))
	label18.grid(row=5,column=6)
	label19 = Label(root12,text="Overall:",pady=10,font=('Helvetica',15,'bold'))
	label19.grid(row=6,column=5)
	label20 = Label(root12,text=Over,pady=10,font=('Helvetica',15,'bold'))
	label20.grid(row=6,column=6)
	label21 = Label(root12,text="Trips:",pady=10,font=('Helvetica',15,'bold'))
	label21.grid(row=7,column=5)
	label22 = Label(root12,text=count,pady=10,font=('Helvetica',15,'bold'))
	label22.grid(row=7,column=6)
	button = Button(root12,text="Logout",command=root12.destroy,pady=10)
	button.grid(row=12,column=1,columnspan=5)
	x = ['Behaviour','Rules','Recommand','Overall','Time']
	y = [Behav,Rul,Recom,Over,Tim]
	fig,ax = plt.subplots(2)
	ax[0].bar(x,y,label='User Ratings',color='Red')
	ax[1].bar('Maximum',Max,width=0.8,label='Maximum Ratings',color='Blue')
	plt.show()
