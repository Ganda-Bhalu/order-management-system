from tkinter import *
from tkinter import font
from types import CoroutineType
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter.font import Font
import sqlite3

root =Tk()
root.title('Order management system')
root.iconbitmap('.\deadpool.ico')
root.geometry("1280x720")

bigfont= Font(family="Helvetica",size=24,weight="bold",slant="roman",underline=0,overstrike=0)

medfont= Font(family="Helvetica",size=12,weight="bold",slant="roman",underline=0,overstrike=0)


def popup():
  messagebox.showinfo("Login Page","Login Successfull!")

def popup1():
  messagebox.askquestion("Reg. Page","Are the details correct?")

def popupcancel():
  messagebox.showinfo("Cancel","Order cancelled successfull!")

def popuptrack():
  messagebox.showinfo("Track","Order on its way!")



def login():
  f2=Frame(bg="#FF4343")
  f2.place(x=0,y=0,width=1280,height=720)
  
  u=Label(f2,text="Login Page",bg="#FF4343",fg="white",font=bigfont)
  u.place(x=150,y=10)

  u1=Label(f2,text="User name",bg="#FF4343",fg="white") 
  u1.place(x=100,y=80)
  e1=Entry(f2,font=("",12))
  e1.place(x=200,y=80,width=160)

  u2=Label(f2,text="Password",bg="#FF4343",fg="white") 
  u2.place(x=100,y=130)
  e2=Entry(f2,font=("",12),show='*')
  e2.place(x=200,y=130,width=160)
  
  
  b3=Button(f2,text="Login",command=popup)
  b3.place(x=200,y=180,width=80,height=40)

  b2=Button(f2,text="<- ",command=home)
  b2.place(x=2,y=3)



def Register():
  f3=Frame(bg="#FF4343")
  f3.place(x=0,y=0,width=1280,height=720)
  u=Label(f3,text="Registration page",bg="#FF4343",fg="white",font=bigfont)
  u.place(x=150,y=10)

  u1=Label(f3,text="Name",bg="#FF4343",fg="white") 
  u1.place(x=100,y=80)
  e1=Entry(f3,font=("",12))
  e1.place(x=200,y=80,width=180)

  u2=Label(f3,text="Address",bg="#FF4343",fg="white") 
  u2.place(x=100,y=130)
  e2=Entry(f3,font=("",12))
  e2.place(x=200,y=130,width=180)
  
  u2=Label(f3,text="Gender",bg="#FF4343",fg="white") 
  u2.place(x=100,y=180)
  r=IntVar()
  r.set("1")
  Radiobutton1=Radiobutton(f3, text="Male",variable=r,value=1).place(x=200,y=180)
  Radiobutton2=Radiobutton(f3, text="Female",variable=r,value=2).place(x=300,y=180)

  u2=Label(f3,text="Mobile no.",bg="#FF4343",fg="white") 
  u2.place(x=100,y=230)
  e2=Entry(f3,font=("",12))
  e2.place(x=200,y=230,width=180)

  u2=Label(f3,text="Email",bg="#FF4343",fg="white") 
  u2.place(x=100,y=280)
  e2=Entry(f3,font=("",12))
  e2.place(x=200,y=280,width=180)


  b3=Button(f3,text="Register",command=popup1)
  b3.place(x=200,y=330,width=80,height=40)

  b2=Button(f3,text="<- ",command=home)
  b2.place(x=2,y=3)



def management():
  f4=Frame(bg="#FF4343")
  f4.place(x=0,y=0,width=1280,height=720)
  b1=Button(f4, text="Place order",command=placeo,borderwidth=3,font=("Helvetica","9"))
  b1.place(x=450,y=360, width=100,height=50)
  b2=Button(f4, text="Track your order",command=tracko,borderwidth=3,font=("Helvetica","9"))
  b2.place(x=580,y=360,width=120,height=50)
  b3=Button(f4, text="Cancel order",command=cancelo,borderwidth=3,font=("Helvetica","9"))
  b3.place(x=730,y=360,width=110,height=50)
  b4=Button(f4,text="<- ",command=home)
  b4.place(x=2,y=3)



def submitorder():


  #Creating database or connect..
  conn=sqlite3.connect('management_system.db')

  #create cursor
  c=conn.cursor()
  
  # Insert into table
  c.execute("INSERT INTO placeorder VALUES(:select_order,:name,:address,:city,:state,:mobile_no,:why_place)",
            {
              'select_order':ordertype.get(),
              'name':name.get(),
              'address':address.get(),
              'city':city.get(),
              'state':state.get(),
              'mobile_no':mobile.get(),
              'why_place':whyplace.get()
            })


  #clearing stuff
  ordertype.set("Select option")
  name.delete(0, END)
  address.delete(0, END)
  city.delete(0, END)
  state.delete(0, END)
  mobile.delete(0, END)
  whyplace.delete(0, END)


  #commit changes
  conn.commit()

  #close connection
  conn.close()
  messagebox.showinfo("Place order","Order is placed successfully!")



def showrecord():
  #Creating database or connect..
  conn=sqlite3.connect('management_system.db')

  #create cursor
  c=conn.cursor()


  # Printing record
  c.execute("SELECT *,oid FROM placeorder")
  f8=Frame(bg="#335CE2")
  f8.place(x=0,y=0,width=1280,height=720)

  u=Label(f8,text="Record data",bg="#335CE2",fg="white",font=bigfont)
  u.grid(row=0,column=0)
  # .place(x=150,y=10)
  
  record1=c.fetchall()
  # print(record1)

  #loop to show record
  print_records=''
  for record in record1:
    print_records += str(record1)+ " " + "\n\n"
  
  screenlabel=Label(f8,text=print_records,bg="#335CE2",fg="#FFFFFF",font=medfont)
  screenlabel.grid(row=1,column=0,columnspan=2,pady=50)
  # .place(x=20,y=70)
  # relx=0.3,rely=0.3

  b2=Button(f8,text="<- ",command=placeo)
  b2.place(x=2,y=3)


  #commit changes
  conn.commit()

  #close connection
  conn.close()



def placeo():
  f5=Frame(bg="#FF4343")
  f5.place(x=0,y=0,width=1280,height=720)
  
  u=Label(f5,text="Place your order",bg="#FF4343",fg="white",font=bigfont)
  u.place(x=150,y=10)

  u1=Label(f5,text="Select your order",bg="#FF4343",fg="white") 
  u1.place(x=80,y=80)
  global ordertype
  ordertype=StringVar()
  ordertype.set("Select option")
  drop=OptionMenu(f5,ordertype,"Select option","Food","Clothes","Electronics","Furniture")
  drop.place(x=200,y=80,width=180)
  
  u2=Label(f5,text="Name",bg="#FF4343",fg="white") 
  u2.place(x=100,y=130)
  global name
  name=Entry(f5,font=("",12))
  name.place(x=200,y=130,width=180)

  u3=Label(f5,text="Address",bg="#FF4343",fg="white") 
  u3.place(x=100,y=180)
  global address
  address=Entry(f5,font=("",12))
  address.place(x=200,y=180,width=180)
  
  u4=Label(f5,text="City",bg="#FF4343",fg="white") 
  u4.place(x=100,y=230)
  global city
  city=Entry(f5,font=("",12))
  city.place(x=200,y=230,width=180)

  u5=Label(f5,text="State",bg="#FF4343",fg="white") 
  u5.place(x=100,y=280)
  global state
  state=Entry(f5,font=("",12))
  state.place(x=200,y=280,width=180)

  u6=Label(f5,text="Mobile no.",bg="#FF4343",fg="white") 
  u6.place(x=80,y=330)
  global mobile
  mobile=Entry(f5,font=("",12))
  mobile.place(x=200,y=330,width=180)

  u7=Label(f5,text="Why place order?",bg="#FF4343",fg="white") 
  u7.place(x=75,y=380)
  global whyplace
  whyplace=Entry(f5,font=("",12))
  whyplace.place(x=200,y=380,width=180)

  # Submit button
  subbutton=Button(f5,text="Submit",command=submitorder)
  subbutton.place(x=200,y=430,width=80,height=40)
  # Back button
  b2=Button(f5,text="<- ",command=management)
  b2.place(x=2,y=3)

  #Create Show record button
  showrec=Button(f5,text="Show record",command=showrecord)
  showrec.place(x=300,y=430,width=100,height=40)



def tracko():
  f6=Frame(bg="#FF4343")
  f6.place(x=0,y=0,width=1280,height=720)
  
  u=Label(f6,text="Track your order",bg="#FF4343",fg="white",font=bigfont)
  u.place(x=150,y=10)

  u1=Label(f6,text="Order history",bg="#FF4343",fg="white") 
  u1.place(x=100,y=80)
  history=StringVar()
  history.set("Select option")
  drop=OptionMenu(f6,history,"Select option","Previous order","Current order")
  drop.place(x=200,y=80,width=180)
  u2=Label(f6,text="Order ID",bg="#FF4343",fg="white") 
  u2.place(x=100,y=130)
  e2=Entry(f6,font=("",12))
  e2.place(x=200,y=130,width=180)
  u2=Label(f6,text="Why track order?",bg="#FF4343",fg="white") 
  u2.place(x=80,y=180)
  e2=Entry(f6,font=("",12))
  e2.place(x=200,y=180,width=180)
  b3=Button(f6,text="Submit",command=popuptrack)
  b3.place(x=200,y=230,width=80,height=40)

  b2=Button(f6,text="<- ",command=management)
  b2.place(x=2,y=3)
  


def deleterecord():

  #Creating database or connect..
  conn=sqlite3.connect('management_system.db')

  #create cursor
  c=conn.cursor()
  
  # Delete Record
  c.execute("DELETE from placeorder WHERE oid = " + cancel_box.get())

  cancel_box.delete(0, END)
  cancel_box2.delete(0, END)

  #commit changes
  conn.commit()

  #close connection
  conn.close()
  messagebox.showinfo("Cancel order","Order is cancelled!!")



def cancelo():
  f7=Frame(bg="#FF4343")
  f7.place(x=0,y=0,width=1280,height=720)
  
  u=Label(f7,text="Cancel your Order",bg="#FF4343",fg="white",font=bigfont)
  u.place(x=150,y=10)

  u1=Label(f7,text="Order ID",bg="#FF4343",fg="white") 
  u1.place(x=100,y=80)
  global cancel_box
  cancel_box=Entry(f7,font=("",12))
  cancel_box.place(x=200,y=80,width=180)
  
  u2=Label(f7,text="Why cancel?",bg="#FF4343",fg="white") 
  u2.place(x=100,y=130)
  global cancel_box2
  cancel_box2=Entry(f7,font=("",12))
  cancel_box2.place(x=200,y=130,width=180)
  
  
  b3=Button(f7,text="Submit",command=deleterecord)
  b3.place(x=200,y=180,width=80,height=40)

  b2=Button(f7,text="<- ",command=management)
  b2.place(x=2,y=3)



def home():

  f1=Frame(bg="#FF4343",)
  f1.place(x=0,y=0,width=1280,height=720)
  b1=Button(f1, text="Login",command=login,font=("Helvetica","9"))
  b1.place(x=450,y=360, width=80,height=50)
  b2=Button(f1, text="Register",command=Register,font=("Helvetica","9"))
  b2.place(x=550,y=360,width=80,height=50)
  b3=Button(f1, text="Order Management",command=management,font=("Helvetica","9"))
  b3.place(x=650,y=360,width=145,height=50)
  

home()

#Database for Management System

#Creating database or connect..
conn=sqlite3.connect('management_system.db')

#create cursor
c=conn.cursor()

#create table
# c.execute(""" CREATE TABLE placeorder (
#           select_order text,
#           name text,
#           address text,
#           city text,
#           state text,
#           mobile_no integer,
#           why_place text 
#               )""")


#commit changes
conn.commit()

#close connection
conn.close()

root.mainloop()