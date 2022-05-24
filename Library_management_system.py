from cgitb import text
from fileinput import close
from msilib import add_data
from multiprocessing import connection
from multiprocessing.sharedctypes import Value
from pickle import FRAME
from sqlite3 import Cursor, connect
from tkinter import*
from tkinter import ttk
from tkinter import font
import tkinter
from tkinter.tix import INTEGER
from turtle import onclick, width
import mysql.connector  
from tkinter import messagebox
import datetime
import tkinter

from mysqlx import Column, Row


class LibraryManagementSystem:
    def __init__(self,root):    
        self.root=root
        self.root.title("Library Management System")    
        self.root.geometry("1550x800+0+0")

        # ==================================variables from mysql==========================================

        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_int=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postid_big=StringVar()
        self.mobile_big=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.borroweddate_var=StringVar()
        self.duedate_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.actualprice_var=StringVar()
         




        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="light blue",fg="red",bd=10,relief=RIDGE,font=("times new roman",40,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=10,relief=RIDGE,padx=20,bg="light blue")
        frame.place(x=0,y=85,width=1530,height=420)
        # ================================Data Frame Left===================================================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="light blue",fg="black",bd=12,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=950,height=390)

        lblmembr=Label(DataFrameLeft,bg="light blue",text="Member Type",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblmembr.grid(row=0,column=0,sticky=W)

        # Create combination box
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",15,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_NO=Label(DataFrameLeft,bg="light blue",text="PRN NO.",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29,textvariable=self.prn_var)
        txtPRN_NO.grid(row=1,column=1)

        lbltitle=Label(DataFrameLeft,bg="light blue",text="ID NO.",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbltitle.grid(row=2,column=0,sticky=W)
        txttitle=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29,textvariable=self.id_int)
        txttitle.grid(row=2,column=1)

        lblFirstname=Label(DataFrameLeft,bg="light blue",text="First Name: ",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblFirstname.grid(row=3,column=0,sticky=W)
        txtFirstname=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29,textvariable=self.firstname_var)
        txtFirstname.grid(row=3,column=1)


        lblLastname=Label(DataFrameLeft,bg="light blue",text="Last Name: ",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblLastname.grid(row=4,column=0,sticky=W)
        txtLastname=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29,textvariable=self.lastname_var)
        txtLastname.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="light blue",text="Address 1: ",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29,textvariable=self.address1_var)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="light blue",text="Address 2: ",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29,textvariable=self.address2_var)
        txtAddress2.grid(row=6,column=1)

        lblPostcode=Label(DataFrameLeft,bg="light blue",text="Post Code: ",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPostcode.grid(row=7,column=0,sticky=W)
        txtPostcode=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29,textvariable=self.postid_big)
        txtPostcode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="light blue",text="Mobile No.",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29,textvariable=self.mobile_big)
        txtMobile.grid(row=8,column=1)

        lblBook_ID=Label(DataFrameLeft,bg="light blue",text="Book ID: ",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblBook_ID.grid(row=0,column=2,sticky=W)
        txtBook_ID=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29,textvariable=self.bookid_var)
        txtBook_ID.grid(row=0,column=3)

        lblBooktitle=Label(DataFrameLeft,bg="light blue",text="Book Title: ",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblBooktitle.grid(row=1,column=2,sticky=W)
        txtBooktitle=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29,textvariable=self.booktitle_var)
        txtBooktitle.grid(row=1,column=3)

        lblAuther=Label(DataFrameLeft,bg="light blue",text="Auhter Name: ",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29,textvariable=self.auther_var)
        txtAuther.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="light blue",text="Borrowed Date: ",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29,textvariable=self.borroweddate_var)
        txtDateBorrowed.grid(row=3,column=3)

        lblDueDate=Label(DataFrameLeft,bg="light blue",text="Due Date: ",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblDueDate.grid(row=4,column=2,sticky=W)
        txtDueDate=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29,textvariable=self.duedate_var)
        txtDueDate.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,bg="light blue",text="Days on Book: ",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29,textvariable=self.daysonbook_var)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="light blue",text="Late Return Fine: ",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29,textvariable=self.latereturnfine_var)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverDue=Label(DataFrameLeft,bg="light blue",text="Date Over Due: ",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29,textvariable=self.dateoverdue_var)
        txtDateOverDue.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,bg="light blue",text="Actual Price: ",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29,textvariable=self.actualprice_var)
        txtActualPrice.grid(row=8,column=3)


        #================================Data Frame Right======================================================

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="light blue",fg="black",bd=12,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameRight.place(x=960,y=5,width=530,height=390)

        # Create TextBox
        self.txtBox=Text(DataFrameRight, font=("times new roman",15,"bold"),width=25,height=14,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)  

        # create scrollbar
        listscrollbar=Scrollbar(DataFrameRight)
        listscrollbar.grid(row=0,column=1,sticky="ns")

        # List of Books
        listbooks=["DBMS","Software Engineering","Computer Graphics","PA","Tools and Weapons","Digital Logic Design and Computer Organization","Engineering Mathematics 3","Let Us C","Let Us CPP","Fluent Python","Information Technology Law","The Soul of New Machine",
                    "Design for Digital","Artificial Intelligence","The Power of Experiments","Blockchain for Bussiness","Algorithm to live By"]

        # Book Dtails
        def SelectBook(event=""):
            value=str(ListBox.get(ListBox.curselection()))
            x=value
            if (x=="DBMS"):
                self.bookid_var.set("BKID001")
                self.booktitle_var.set("DBMS")
                self.auther_var.set("Rajiv Chopra")


                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.439")

            elif (x=="Software Engineering"):
                self.bookid_var.set("BKID002")
                self.booktitle_var.set("Software Engineering")
                self.auther_var.set("Sommerville Ian")


                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.670")

            elif (x=="Computer Graphics"):
                self.bookid_var.set("BKID003")
                self.booktitle_var.set("Computer Graphics")
                self.auther_var.set("Donald D.Hearn")


                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.485")

            
            elif (x=="PA"):
                self.bookid_var.set("BKID004")
                self.booktitle_var.set("PA")
                self.auther_var.set("A. P. Godse")


                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.295")

        
            elif (x=="Tools and Weapons"):
                self.bookid_var.set("BKID005")
                self.booktitle_var.set("Tools and Weapons")
                self.auther_var.set("Brad Smith")


                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.1147")

            
            elif (x=="Digital Logic Design and Computer Organization"):
                self.bookid_var.set("BKID006")
                self.booktitle_var.set("Digital Logic Design and Computer Organization")
                self.auther_var.set("V. Rajaraman")


                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.280")


            elif (x=="Engineering Mathematics 3"):
                self.bookid_var.set("BKID007")
                self.booktitle_var.set("Engineering Mathematics 3")
                self.auther_var.set("Dr.M.Y.Gokhale")


                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.550")


            elif (x=="Let Us C"):
                self.bookid_var.set("BKID008")
                self.booktitle_var.set("Let Us C")
                self.auther_var.set("Yashwant Kanetkar")


                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.350")


            elif (x=="Let Us CPP"):
                self.bookid_var.set("BKID009")
                self.booktitle_var.set("Let Us CPP")
                self.auther_var.set("Yashwant Kanetkar")


                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.400")


            elif (x=="Fluent Python"):
                self.bookid_var.set("BKID010")
                self.booktitle_var.set("Fluent Python")
                self.auther_var.set("Lucian Ramalho")


                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.1950")


            elif (x=="Information Technology Law"):
                self.bookid_var.set("BKID011")
                self.booktitle_var.set("Information Technology Law")
                self.auther_var.set("Vakul Sharma")


                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.718")


           
            elif (x=="The Soul of New Machine"):
                self.bookid_var.set("BKID012")
                self.booktitle_var.set("The Soul of Machine")
                self.auther_var.set("Tracy Kidder")


                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.1200")


            elif (x=="Design for Digital"):
                self.bookid_var.set("BKID013")
                self.booktitle_var.set("Design for Degital")
                self.auther_var.set("Jeanne W. Ross")


                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.2238")


            elif (x=="Artificial Intelligence"):
                self.bookid_var.set("BKID014")
                self.booktitle_var.set("Artificial Intelligence")
                self.auther_var.set("Purva Raut")


                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.214")


            elif (x=="The Power of Experiments"):
                self.bookid_var.set("BKID015")
                self.booktitle_var.set("The Power of Experiments")
                self.auther_var.set("Max H. Bazerman")


                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.1500")


            elif (x=="Blockchain for Bussiness"):
                self.bookid_var.set("BKID016")
                self.booktitle_var.set("Blockchain for Bussiness")
                self.auther_var.set("Jai Singh Arun")


                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.399")


            elif (x=="Algorithm to live By"):
                self.bookid_var.set("BKID017")
                self.booktitle_var.set("Algorithm to live By")
                self.auther_var.set("Brian Christian")


                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.319")


             
                

             





        # Create listBox
        ListBox=Listbox(DataFrameRight, font=("times new roman",15,"bold"),width=20,height=14)
        ListBox.bind("<<ListboxSelect>>",SelectBook)
        ListBox.grid(row=0,column=0,padx=4)
        listscrollbar.config(command=ListBox.yview)

        # Add Book Name in listBox
        for item in listbooks:             
            ListBox.insert(END,item)
       


            # =================================Buttons Frame=====================================================

        framebuttons=Frame(self.root,bd=10,relief=RIDGE,padx=20,bg="light blue")
        framebuttons.place(x=0,y=498,width=1530,height=100)

        btnAddData=Button(framebuttons,command=self.adda_data,text="Add Data",font=("times new roman",15,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(framebuttons,command=self.showData,text="Show Data",font=("times new roman",15,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(framebuttons,command=self.update,text="Update",font=("times new roman",15,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(framebuttons,command=self.delete,text="Delete",font=("times new roman",15,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(framebuttons,command=self.reset,text="Reset",font=("times new roman",15,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(framebuttons,command=self.iExit,text="Exit",font=("times new roman",15,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)

        # =================================Information Frame/ Bottom Frame=====================================================

        frameinf=Frame(self.root,bd=10,relief=RIDGE,padx=20,bg="light blue")
        frameinf.place(x=0,y=560,width=1530,height=220)

        # frame inside the Bottom frame
        table_frame=Frame(frameinf,bd=6,relief=RIDGE,padx=20,bg="light blue")
        table_frame.place(x=0,y=2,width=1460,height=190)

        #Scrollbar in table frame
        xscroll=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(table_frame,orient=VERTICAL)

        # Data in Heading
        self.library_table=ttk.Treeview(table_frame,column=("membertype","prnno","title","firstname","lastname","address1","address2","postcode"
                                                            ,"mobile","bookid","booktitle","auther","borroweddate","duedate","daysonbook"
                                                            ,"latereturnfine","dateoverdue","actualprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set )

        # set scrollbar at bottom and right side
        xscroll.pack(side=BOTTOM,fill=X)        
        yscroll.pack(side=RIGHT,fill=Y)     

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)                                                     

        self.library_table.heading("membertype",text="Member Type") 
        self.library_table.heading("prnno",text="PRN NO.")
        self.library_table.heading("title",text="Title")                                                   
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address 1") 
        self.library_table.heading("address2",text="Address 2")
        self.library_table.heading("postcode",text="Post Code")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("borroweddate",text="Borrowed Date")
        self.library_table.heading("duedate",text="Due Date")
        self.library_table.heading("daysonbook",text="Days on Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("actualprice",text="Actual Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postcode",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("borroweddate",width=100)
        self.library_table.column("duedate",width=100)
        self.library_table.column("daysonbook",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("actualprice",width=100)

        # when we add data in the table it will automatically show in bottom frame
        self.fatch_data()

        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

        # Add data button
    def adda_data(self):
        connection=mysql.connector.connect(host="localhost",username="root",password="Sujit@1234",database="mydata")
        mycursor=connection.cursor()
        mycursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                    self.member_var.get(),
                                                                                                                    self.prn_var.get(),
                                                                                                                    self.id_int.get(),
                                                                                                                    self.firstname_var.get(),
                                                                                                                    self.lastname_var.get(),
                                                                                                                    self.address1_var.get(),
                                                                                                                    self.address2_var.get(),
                                                                                                                    self.postid_big.get(),
                                                                                                                    self.mobile_big.get(),
                                                                                                                    self.bookid_var.get(),
                                                                                                                    self.booktitle_var.get(),
                                                                                                                    self.auther_var.get(),
                                                                                                                    self.borroweddate_var.get(),
                                                                                                                    self.duedate_var.get(),
                                                                                                                    self.daysonbook_var.get(),
                                                                                                                    self.latereturnfine_var.get(),
                                                                                                                    self.dateoverdue_var.get(),
                                                                                                                    self.actualprice_var.get()
                                                                                                                ))
        
        connection.commit()
        self.fatch_data()
        connection.close()
                                                                                                                
        
        # to display the message after clicking add data
        messagebox.showinfo("Success","Member has been inserted Successfully")

        # Update Button
    def update(self):
        connection=mysql.connector.connect(host="localhost",username="root",password="Sujit@1234",database="mydata")
        mycursor=connection.cursor()
        mycursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostId=%s,Mobile=%s,Bookid=%s,Booktitle=%s,Auther=%s,Borroweddate=%s,Duedate=%s,Daysonbook=%s,Latereturnfine=%s,Dateoverdue=%s,Actualprice=%s where PRN_NO=%s", (
                                                                                                                    self.member_var.get(), 
                                                                                                                    self.id_int.get(),
                                                                                                                    self.firstname_var.get(),
                                                                                                                    self.lastname_var.get(),
                                                                                                                    self.address1_var.get(),
                                                                                                                    self.address2_var.get(),
                                                                                                                    self.postid_big.get(),
                                                                                                                    self.mobile_big.get(),
                                                                                                                    self.bookid_var.get(),
                                                                                                                    self.booktitle_var.get(),
                                                                                                                    self.auther_var.get(),
                                                                                                                    self.borroweddate_var.get(),
                                                                                                                    self.duedate_var.get(),
                                                                                                                    self.daysonbook_var.get(),
                                                                                                                    self.latereturnfine_var.get(),
                                                                                                                    self.dateoverdue_var.get(),
                                                                                                                    self.actualprice_var.get(),
                                                                                                                    self.prn_var.get()
                                                                                                                    

                                                                                                                ))

        connection.commit()
        self.fatch_data()
        self.reset()
        connection.close()

        #to show message of update
        messagebox.showinfo("Success","Member has been Updated")
                                                                  


        # to collect data from library table to bottom frame
    def fatch_data(self):
        connection=mysql.connector.connect(host="localhost",username="root",password="Sujit@1234",database="mydata")
        mycursor=connection.cursor()
        mycursor.execute("select *from library")
        rows=mycursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())  # to delete the current data in table
            for i in rows:                                                 # to insert new data in table
                self.library_table.insert("",END,values=i)

            connection.commit()
        connection.close()

        # when we click on any data at bottom it will show in entry column

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_int.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postid_big.set(row[7]),
        self.mobile_big.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.borroweddate_var.set(row[12]),
        self.duedate_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.actualprice_var.set(row[17])


        # Show Data Button
    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+self.member_var.get()+ "\n")
        self.txtBox.insert(END,"PRN NO.:\t\t"+self.prn_var.get()+ "\n")
        self.txtBox.insert(END,"ID NO.:\t\t"+self.id_int.get()+ "\n")
        self.txtBox.insert(END,"First Name:\t\t"+self.firstname_var.get()+ "\n")
        self.txtBox.insert(END,"Last Name:\t\t"+self.lastname_var.get()+ "\n")
        self.txtBox.insert(END,"Address 1:\t\t"+self.address1_var.get()+ "\n")
        self.txtBox.insert(END,"Address 2:\t\t"+self.address2_var.get()+ "\n")
        self.txtBox.insert(END,"Post Code:\t\t"+self.postid_big.get()+ "\n")
        self.txtBox.insert(END,"Mobile No.:\t\t"+self.mobile_big.get()+ "\n")
        self.txtBox.insert(END,"Book ID:\t\t"+self.bookid_var.get()+ "\n")
        self.txtBox.insert(END,"Book Title:\t\t"+self.booktitle_var.get()+ "\n")
        self.txtBox.insert(END,"Auther Name:\t\t"+self.auther_var.get()+ "\n")
        self.txtBox.insert(END,"Borrowed Date:\t\t"+self.borroweddate_var.get()+ "\n")
        self.txtBox.insert(END,"Due Date:\t\t"+self.duedate_var.get()+ "\n")
        self.txtBox.insert(END,"Days on Book:\t\t"+self.daysonbook_var.get()+ "\n")
        self.txtBox.insert(END,"Late Return Fine:\t\t"+self.latereturnfine_var.get()+ "\n")
        self.txtBox.insert(END,"Date Over Due:\t\t"+self.dateoverdue_var.get()+ "\n")
        self.txtBox.insert(END,"Actual Price:\t\t"+self.actualprice_var.get()+ "\n")

        # Reset Button
    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_int.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postid_big.set(""),
        self.mobile_big.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.borroweddate_var.set(""),
        self.duedate_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.actualprice_var.set(""),
        self.txtBox.delete("1.0",END)


        # Exit Button
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to Exit")
        if iExit>0:
            self.root.destroy()
            return

        # Delete Button
    def delete(self):
        i=self.prn_var.get()
        if i=="":
            messagebox.showerror("Error","First select the Member")
        else:
            connection=mysql.connector.connect(host="localhost",username="root",password="Sujit@1234",database="mydata")
            mycursor=connection.cursor()
            query="delete from library where PRN_NO=%s"
            Value=(self.prn_var.get(),)
            mycursor.execute(query,Value)

            connection.commit()
            self.fatch_data()
            self.reset()
            connection.close()

            # delete message
            messagebox.showinfo("Success","Member has been Deleted")

        
    

    
    
        

                    



if __name__=="__main__":    
    root=Tk()
    object=LibraryManagementSystem(root)
    root.mainloop() 
