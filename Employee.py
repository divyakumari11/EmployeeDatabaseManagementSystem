from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import time;
import tempfile,os
import EmployeeDatabase
#========================================Frontend============================================================
class Employee:
    def __init__(self,roo):
        self.root = root
        self.root.title("Employee Database Management System")
        self.root.geometry("1350x800+0+0")
        self.root.configure (bg = 'dodger blue4')

        MainFrame = Frame(self.root, bd = 10,width =2500, height = 700,bg='dodger blue4',relief= GROOVE)
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame, bd = 7,width =1340, height = 100,bg='dodger blue4',relief=GROOVE)
        TopFrame1.grid(row = 2, column = 0)

        TopFrame2 = Frame(MainFrame, bd = 7,width =1340, height = 100,bg='dodger blue4',relief=GROOVE)
        TopFrame2.grid(row = 1,column = 0)

        TopFrame3 = Frame(MainFrame, bd = 7,width =1340, height = 500,bg='dodger blue4',relief=GROOVE)
        TopFrame3.grid(row = 0,column = 0)

        LeftFrame = Frame(TopFrame3,bd=5, width = 1340,height=400,padx=2,bg='dodger blue4',relief=GROOVE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame,bd=5, width = 600,height=200,padx=4,pady=4,bg='dodger blue4',relief=GROOVE)
        LeftFrame1.pack(side=TOP)

        LeftFrame2 = Frame(LeftFrame,bd=5, width = 600,height=200,padx=4,pady=4,bg='dodger blue4',relief=GROOVE)
        LeftFrame2.pack(side=TOP)
        LeftFrame2Left = Frame(LeftFrame,bd=5, width = 300,height=170,padx=2,bg='dodger blue4',relief=GROOVE)
        LeftFrame2Left.pack(side=LEFT)
        LeftFrame2Right = Frame(LeftFrame2,bd=5, width = 300,height=170,padx=2,bg='dodger blue4',relief=GROOVE)
        LeftFrame2Right.pack(side=RIGHT)

        RightFrame1 = Frame(TopFrame3,bd=5, width = 320,height=400,padx=2,bg='cadet blue',relief=GROOVE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1,bd=5, width = 310,height=300,padx=2,bg='cadet blue',relief=GROOVE)
        RightFrame1a.pack(side=TOP)
        RightFrame2 = Frame(TopFrame3,bd=5, width = 300,height=400,padx=2,bg='cadet blue',relief=GROOVE)
        RightFrame2.pack(side=RIGHT)
        RightFrame2a = Frame(RightFrame2,bd=5, width = 280,height=100,padx=2,bg='cadet blue',relief=GROOVE)
        RightFrame2a.pack(side=TOP)
        RightFrame2b = Frame(RightFrame2,bd=5, width = 280,height=100,padx=2,bg='cadet blue',relief=GROOVE)
        RightFrame2b.pack(side=TOP)
        RightFrame2c = Frame(RightFrame2,bd=5, width = 280,height=100,padx=2,bg='cadet blue',relief=GROOVE)
        RightFrame2c.pack(side=TOP)
        RightFrame2d = Frame(RightFrame2,bd=5, width = 280,height=100,padx=2,bg='cadet blue',relief=GROOVE)
        RightFrame2d.pack(side=TOP)
        #==========================================Variables==================================================================
        global Ed
        Firstname =StringVar()
        Surname =StringVar()
        Address =StringVar()
        CityWeighting = IntVar()
        Mobile =StringVar()
        Email =StringVar()
        BasicSalary=IntVar()
        OverTime=StringVar()
        GrossPay=StringVar()
        NetPay=StringVar()
        Tax=StringVar()
        Pension=StringVar()
        stdLoan = StringVar()
        NIPayment=StringVar()
        Deductions=StringVar()
        Gender=StringVar()
        Payday=StringVar()
        TaxPeriod=StringVar()
        NINumber=StringVar()
        NICode=StringVar()
        TaxablePay=StringVar()
        PensionablePay=StringVar()
        OtherPaymentDue=StringVar()
        TaxCode=StringVar()
        Reference=StringVar()
        StudentLoan=StringVar()
        CityWeighting.set("")
        BasicSalary.set("")
        OtherPaymentDue.set("0.00")
        OverTime=StringVar()

        #====================================================Functions====================================================
        def addData ():
            if(len(Reference.get())!=0):
                EmployeeDatabase.addEmployeeRec(Reference.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(),
                Mobile.get(),NINumber.get(), stdLoan.get(),Tax.get(),Pension.get(),Deductions.get(),NetPay.get(),GrossPay.get())
                lstEmployee.delete(0,END)
                lstEmployee.insert(END,(Reference.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),
                            NINumber.get(),stdLoan.get(),Tax.get(),Pension.get(),Deductions.get(),NetPay.get(),GrossPay.get()))

        def DisplayData():
            lstEmployee.delete(0,END)
            for row in EmployeeDatabase.viewData():
                lstEmployee.insert(END,row,str(""))

        def EmployeeRec(event):
            global Ed
            searchEd = lstEmployee.curselection()[0]
            Ed = lstEmployee.get(searchEd)

            self.txtReference.delete(0,END)
            self.txtReference.insert(END,Ed[1])
            self.txtFirstname.delete(0,END)
            self.txtFirstname.insert(END,Ed[2])
            self.txtSurname.delete(0,END)
            self.txtSurname.insert(END,Ed[3])
            self.txtAddress.delete(0,END)
            self.txtAddress.insert(END,Ed[4])
            self.txtGender.delete(0,END)
            self.txtGender.insert(END,Ed[5])
            self.txtMobile.delete(0,END)
            self.txtMobile.insert(END,Ed[6])
            self.txtNINumber.delete(0,END)
            self.txtNINumber.insert(END,Ed[7])
            self.txtstdLoan.delete(0,END)
            self.txtstdLoan.insert(END,Ed[8])
            self.txtTax.delete(0,END)
            self.txtTax.insert(END,Ed[9])
            self.txtPension.delete(0,END)
            self.txtPension.insert(END,Ed[10])
            self.txtDeductions.delete(0,END)
            self.txtDeductions.insert(END,Ed[11])
            self.txtNetPay.delete(0,END)
            self.txtNetPay.insert(END,Ed[12])
            self.txtGrossPay.delete(0,END)
            self.txtGrossPay.insert(END,Ed[13])

        def DeleteData():
            if(len(Reference.get())!=0):
                EmployeeDatabase.deleteRec(Ed[0])
                Reset()
                DisplayData()

        def SearchData():
            lstEmployee.delete(0,END)
            for row in EmployeeDatabase.searchData(Reference.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(),
                                                   Mobile.get(),
                NINumber.get(),stdLoan.get(),Tax.get(),Pension.get(),Deductions.get(),NetPay.get(),GrossPay.get()):
                lstEmployee.insert(END,row,str(""))

        def update():
            if(len(Reference.get())!=0):
                EmployeeDatabase.deleteRec(Ed[0])
            if(len(Reference.get())!=0):
                EmployeeDatabase.addEmployeeRec(Reference.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),NINumber.get(),stdLoan.get(),Tax.get(),Pension.get(),Deductions.get(),NetPay.get(),GrossPay.get())
                lstEmployee.delete(0,END)
                lstEmployee.insert(END,(Reference.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(), Mobile.get(),
                NINumber.get(),stdLoan.get(),Tax.get(),Pension.get(),Deductions.get(),NetPay.get(),GrossPay.get()))

        def iPrint():
            q=self.txtReceipt.get("1.0","end-1c")
            filename=tempfile.mktemp(".doc")
            open (filename, "w").write(q)
            os.startfile(filename, "print")

        def Reset():
            Firstname.set("")
            Surname.set("")
            Address.set("")
            CityWeighting.set("")
            Mobile.set("")
            Email.set("")
            BasicSalary.set("")
            OverTime.set("")
            GrossPay.set("")
            NetPay.set("")
            Tax.set("")
            Pension.set("")
            stdLoan.set("")
            NIPayment.set("")
            Deductions.set("")
            Gender.set("")
            Payday.set("")
            TaxPeriod.set("")
            NINumber.set("")
            NICode.set("")
            TaxablePay.set("")
            PensionablePay.set("")
            OtherPaymentDue.set("")
            TaxCode.set("")
            Reference.set("")
            StudentLoan.set("")
            CityWeighting.set("")
            BasicSalary.set("")
            OtherPaymentDue.set("0.00")
            OverTime.set("")
            self.txtReceipt.delete("1.0",END)

        def iQuit():
            iQuit =tkinter.messagebox.askyesno("Employee Database System","Confirm if you want to exit")
            if iQuit > 0:
                root.destroy()
                return
        def PayRef():
           Payday.set(time.strftime("%d/%m/%Y"))
           Refpay = random.randint(16462,708488)
           Refpaid = ("Ref" + str(Refpay))
           Reference.set(Refpaid)

           NIpay = random.randint(34051,409785)
           NIpaid = ("NI" +str(NIpay))
           NINumber.set(NIpay)

           iDate = datetime.now()
           TaxPeriod.set(iDate.month)

           NCode = random.randint(1290,13123)
           CodeNI = ("NIC" + str(NCode))
           NICode.set(CodeNI)

           iTaxCode = random.randint(7589,15875)
           PaymentTaxCode =("TCode" +str(iTaxCode))
           TaxCode.set(PaymentTaxCode)

        def MonthlySalary():
            PayRef()

            BS = float (BasicSalary.get())
            CW = float (CityWeighting.get())
            OT = float(OverTime.get())
            OPD = float(OtherPaymentDue.get())
            MTax = ((BS + CW + OT + OPD) *0.3)
            TTax = "$",str('%.2f'%(MTax))
            Tax.set(TTax)

            M_Pension = ((BS + CW + OT + OPD)*0.02)
            MM_Pension = "$", str('%.2f'%(M_Pension))
            Pension.set(MM_Pension)

            M_stdLoan = ((BS + CW + OT + OPD) * 0.012)
            MM_stdLoan = "$", str('%.2f'%(M_stdLoan))
            stdLoan.set(MM_stdLoan)

            M_NIPayment = ((BS + CW + OT + OPD) * 0.011)
            MM_NIPayment = "$", str('%.2f'%(M_NIPayment))
            stdLoan.set(MM_NIPayment)

            Deduct = (MTax + M_Pension + M_stdLoan +M_NIPayment)
            Deduct_Payment = "$", str('%.2f'%(Deduct))
            Deductions.set(Deduct_Payment)
            Gross_Pay ="$",str('%.2f' % (BS + CW + OT + OPD))
            GrossPay.set(Gross_Pay)

            NetPayAfter = (BS +CW + OT +OPD) - Deduct
            NetAfter = "$",str("%.2f" % (NetPayAfter))
            NetPay.set(NetAfter)

            TaxablePay.set(TTax)
            PensionablePay.set(MM_Pension)

            self.txtReceipt.insert(END,'\t\t Monthly Pay Slip' + "\n\n")
            self.txtReceipt.insert(END,'Reference:\t\t\t' + Reference.get() +"\n")
            self.txtReceipt.insert(END,'Reference:\t\t\t' + Payday.get() + "\n")
            self.txtReceipt.insert(END,'Employee Name:\t\t\t' + Firstname.get() + "\n")
            self.txtReceipt.insert(END,'Employee Name:\t\t\t' + Surname.get() + "\n")
            self.txtReceipt.insert(END,'Tax:\t\t\t' + Tax.get() + "\n")
            self.txtReceipt.insert(END,'Pension:\t\t\t' + Pension.get() + "\n")
            self.txtReceipt.insert(END,'Student Loan:\t\t\t' + stdLoan.get() + "\n")
            self.txtReceipt.insert(END,'NI Number:\t\t\t' + NINumber.get() + "\n")
            self.txtReceipt.insert(END,'NI Payment:\t\t\t' + NIPayment.get() + "\n")
            self.txtReceipt.insert(END,'Deductions:\t\t\t' + Deductions.get() + "\n")
            self.txtReceipt.insert(END,'City Weighting:\t\t\t' + str('$ %.2f'%(CityWeighting.get())) + "\n")

            self.txtReceipt.insert(END,'Tax Paid:\t\t\t' + str('$ %.2f'%(BasicSalary.get())) + "\n")
            self.txtReceipt.insert(END,'OverTime:\t\t\t' + "$" + OverTime.get() +  "\n")
            self.txtReceipt.insert(END,'NetPay:\t\t\t' + NetPay.get() + "\n")
            self.txtReceipt.insert(END,'City Weighting:\t\t\t' + GrossPay.get() + "\n")
            addData()
#=================================================Receipt=====================================================
        self.txtReceipt = Text(RightFrame1a,height=23,width=42,bd=10,font=('arial',9,'bold'))
        self.txtReceipt.grid(row=0,column=0)
#=============================================================================================================
        self.lbLabel = Label(TopFrame2, font=('arial',10,'bold'),padx=6,pady=2,bg='dodger blue4',
        text = "Reference\tFirstname\tSurname\tAddress\t\tGender\tMobile\tNINumber\tStudent Loan\tTax\tPension\tDeductions\tNet Pay\t\tGrossPay")
        self.lbLabel.grid(row = 0,column =0,columnspan = 17)
#================================================ListBox and Scrollbar==========Receipt==================================================

        scrollbar = Scrollbar(TopFrame2)
        scrollbar.grid(row=1,column=1,sticky='ns')

        lstEmployee = Listbox(TopFrame2, width = 145,height=5,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        lstEmployee.bind('<<ListboxSelect>>',EmployeeRec)
        lstEmployee.grid(row=1,column=0,padx=1,sticky='nsew')
        scrollbar.config(command = lstEmployee.xview)
#=================================================Widget=============================================================
        self.lblReference= Label(LeftFrame1,font=('arial',12,'bold'),text="Referrence",bd=7,bg='cadet blue',anchor='w')
        self.lblReference.grid(row=0,column=0,sticky=W,padx=5)
        self.txtReference= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Reference)
        self.txtReference.grid(row=0,column=1)

        self.lblFirstname= Label(LeftFrame1,font=('arial',12,'bold'),text="Firstname",bd=7,bg='cadet blue',anchor='w')
        self.lblFirstname.grid(row=1,column=0,sticky=W,padx=5)
        self.txtFirstname= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Firstname)
        self.txtFirstname.grid(row=1,column=1)

        self.lblSurname= Label(LeftFrame1,font=('arial',12,'bold'),text="Surname",bd=7,bg='cadet blue', justify='left')
        self.lblSurname.grid(row=2,column=0,sticky=W,padx=5)
        self.txtSurname= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Surname)
        self.txtSurname.grid(row=2,column=1)

        self.lblAddress= Label(LeftFrame1,font=('arial',12,'bold'),text="Address",bd=7,bg='cadet blue')
        self.lblAddress.grid(row=3,column=0,sticky=W,padx=5)
        self.txtAddress= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Address)
        self.txtAddress.grid(row=3,column=1)

        self.lblGender= Label(LeftFrame1,font=('arial',12,'bold'),text="Gender",bd=7,bg='cadet blue')
        self.lblGender.grid(row=4,column=0,sticky=W,padx=5)
        self.txtGender= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Gender)
        self.txtGender.grid(row=4,column=1)

        self.lblMobile= Label(LeftFrame1,font=('arial',12,'bold'),text="Mobile",bd=7,bg='cadet blue')
        self.lblMobile.grid(row=5,column=0,sticky=W,padx=5)
        self.txtMobile= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Mobile)
        self.txtMobile.grid(row=5,column=1)
#====================================================================================================================
        self.lblCityWeighting= Label(LeftFrame2Left,font=('arial',12,'bold'),text="City Weighting",bd=7,bg="cadet blue",anchor='e')
        self.lblCityWeighting.grid(row=0,column=0,sticky=W)
        self.txtCityWeighting= Entry(LeftFrame2Left,font=('arial',12,'bold'),bd=5,width=20, justify='left',textvariable=CityWeighting)
        self.txtCityWeighting.grid(row=0,column=1)

        self.lblBasicSalary= Label(LeftFrame2Left,font=('arial',12,'bold'),text="Basic Salary",bd=7,bg="cadet blue",anchor='w',justify='left')
        self.lblBasicSalary.grid(row=1,column=0,sticky=W)
        self.txtBasicSalary= Entry(LeftFrame2Left,font=('arial',12,'bold'),bd=5,width=20, justify='left',textvariable=BasicSalary)
        self.txtBasicSalary.grid(row=1,column=1)

        self.lblOverTime= Label(LeftFrame2Left,font=('arial',12,'bold'),text="Over Time",bd=7,bg="cadet blue",anchor='w',justify='left')
        self.lblOverTime.grid(row=2,column=0,sticky=W)
        self.txtOverTime= Entry(LeftFrame2Left,font=('arial',12,'bold'),bd=5,width=20, justify='left',textvariable=OverTime)
        self.txtOverTime.grid(row=2,column=1)

        self.lblOtherPaymentDue= Label(LeftFrame2Left,font=('arial',12,'bold'),text="Other Payment",bd=7,bg="cadet blue",anchor='w',justify='left')
        self.lblOtherPaymentDue.grid(row=2,column=0,sticky=W)
        self.txtOtherPaymentDue= Entry(LeftFrame2Left,font=('arial',12,'bold'),bd=5,width=20, justify='left',textvariable=OtherPaymentDue)
        self.txtOtherPaymentDue.grid(row=3,column=1)
#======================================================================================================================
        self.lblTax = Label(LeftFrame2Right,font=('arial',12,'bold'),text="Tax",bd=7,bg="cadet blue",anchor='e')
        self.lblTax.grid(row=0,column=0,sticky=W)
        self.txtTax =Entry(LeftFrame2Right,font=('arial',12,'bold'),bd=5,width=20,justify='left',textvariable=Tax)
        self.txtTax.grid(row=0,column=1)

        self.lblPension = Label(LeftFrame2Right,font=('arial',12,'bold'),text="Pension",bd=7,bg="cadet blue",anchor='w',justify='left')
        self.lblPension.grid(row=1,column=0,sticky=W)
        self.txtPension =Entry(LeftFrame2Right,font=('arial',12,'bold'),bd=5,width=20,justify='left',textvariable=Pension)
        self.txtPension.grid(row=1,column=1)

        self.lblstdLoan = Label(LeftFrame2Right,font=('arial',12,'bold'),text="Student Loan",bd=7,bg="cadet blue",anchor='w',justify='left')
        self.lblstdLoan.grid(row=2,column=0,sticky=W)
        self.txtstdLoan =Entry(LeftFrame2Right,font=('arial',12,'bold'),bd=5,width=20,justify='left',textvariable=StudentLoan)
        self.txtstdLoan.grid(row=2,column=1)

        self.lblNIPayment = Label(LeftFrame2Right,font=('arial',12,'bold'),text="NI Payment",bd=7,bg="cadet blue",anchor='w',justify='left')
        self.lblNIPayment.grid(row=3,column=0,sticky=W)
        self.txtNIPayment =Entry(LeftFrame2Right,font=('arial',12,'bold'),bd=5,width=20,justify='left',textvariable=NIPayment)
        self.txtNIPayment.grid(row=3,column=1)
#=================================================================================================================================================
        self.lblPayday = Label(RightFrame2a,font=('arial',12,'bold'),text="Payday",bd=7,bg="cadet blue",anchor='w',justify='left')
        self.lblPayday.grid(row=0,column=0,sticky=W)
        self.txtPayday =Entry(RightFrame2a,font=('arial',12,'bold'),bd=5,width=20,justify='left',textvariable=Payday)
        self.txtPayday.grid(row=0,column=1)

        self.lblTaxPeriod = Label(RightFrame2a,font=('arial',12,'bold'),text="Tax Period",bd=7,bg="cadet blue",anchor='w',justify='left')
        self.lblTaxPeriod.grid(row=1,column=0,sticky=W)
        self.TaxPeriod =Entry(RightFrame2a,font=('arial',12,'bold'),bd=5,width=20,justify='left',textvariable=TaxPeriod)
        self.TaxPeriod.grid(row=1,column=1)

        self.lblTaxCode = Label(RightFrame2b,font=('arial',12,'bold'),text="Tax Code",bd=7,bg="cadet blue",anchor='w',justify='left')
        self.lblTaxCode.grid(row=2,column=0,sticky=W)
        self.txtTaxCode =Entry(RightFrame2b,font=('arial',12,'bold'),bd=5,width=20,justify='left',textvariable=TaxCode)
        self.txtTaxCode.grid(row=2,column=1)

        self.lblNINumber = Label(RightFrame2b,font=('arial',12,'bold'),text="NI Number",bd=7,bg="cadet blue",anchor='w',justify='left')
        self.lblNINumber.grid(row=3,column=0,sticky=W)
        self.txtNINumber=Entry(RightFrame2b,font=('arial',12,'bold'),bd=5,width=20,justify='left',textvariable=NINumber)
        self.txtNINumber.grid(row=3,column=1)

        self.lblNICode = Label(RightFrame2b,font=('arial',12,'bold'),text="NI Code",bd=7,bg="cadet blue",anchor='w',justify='left')
        self.lblNICode.grid(row=4,column=0,sticky=W)
        self.txtNICode=Entry(RightFrame2b,font=('arial',12,'bold'),bd=5,width=20,justify='left',textvariable=NICode)
        self.txtNICode.grid(row=4,column=1)

        self.lblTaxablePay = Label(RightFrame2c,font=('arial',12,'bold'),text="Taxable Pay",bd=7,bg="cadet blue",anchor='w',justify='left')
        self.lblTaxablePay.grid(row=0,column=0,sticky=W)
        self.txtTaxablePay=Entry(RightFrame2c,font=('arial',12,'bold'),bd=5,width=20,justify='left',textvariable=TaxablePay)
        self.txtTaxablePay.grid(row=0,column=1)

        self.lblNINumber = Label(RightFrame2c,font=('arial',12,'bold'),text="NI Number",bd=7,bg="cadet blue",anchor='w',justify='left')
        self.lblNINumber.grid(row=1,column=0,sticky=W)
        self.txtNINumber=Entry(RightFrame2c,font=('arial',12,'bold'),bd=5,width=20,justify='left',textvariable=NINumber)
        self.txtNINumber.grid(row=1,column=1)

        self.lblPensionablePay = Label(RightFrame2c,font=('arial',12,'bold'),text="Pensionable Pay",bd=7,bg="cadet blue",anchor='w',justify='left')
        self.lblPensionablePay.grid(row=2,column=0,sticky=W)
        self.txtPensionablePay=Entry(RightFrame2c,font=('arial',12,'bold'),bd=5,width=20,justify='left',textvariable=PensionablePay)
        self.txtPensionablePay.grid(row=2,column=1)

        self.lblNetPay = Label(RightFrame2d,font=('arial',12,'bold'),text="Net Pay",bd=7,bg="cadet blue",anchor='w',justify='left')
        self.lblNetPay.grid(row=1,column=0,sticky=W)
        self.txtNetPay=Entry(RightFrame2d,font=('arial',12,'bold'),bd=5,width=17,justify='left',textvariable=NetPay)
        self.txtNetPay.grid(row=1,column=1)

        self.lblGrossPay = Label(RightFrame2d,font=('arial',12,'bold'),text="Gross Pay",bd=7,bg="cadet blue",anchor='w',justify='left')
        self.lblGrossPay.grid(row=2,column=0,sticky=W)
        self.txtGrossPay=Entry(RightFrame2d,font=('arial',12,'bold'),bd=5,width=17,justify='left',textvariable=GrossPay)
        self.txtGrossPay.grid(row=2,column=1)

        self.lblDeductions = Label(RightFrame2d,font=('arial',12,'bold'),text="Deductions",bd=7,bg="cadet blue",anchor='w',justify='left')
        self.lblDeductions.grid(row=3,column=0,sticky=W)
        self.txtDeductions=Entry(RightFrame2d,font=('arial',12,'bold'),bd=5,width=17,justify='left',textvariable=Deductions)
        self.txtDeductions.grid(row=3,column=1)
#=====================================================================Buttons for the topframe1====================================================================================
        self.btnAddNewTotal=Button(TopFrame1,pady=1,bd=4,fg="black",font=('arial',16,'bold'),padx=24,bg='dodger blue',
                            width=8,text="AddNew/Total",command=MonthlySalary).grid(row=0,column=1,padx=1)
        self.btnPrint=Button(TopFrame1,pady=1,bd=4,fg="black",font=('arial',16,'bold'),padx=24,bg='dodger blue',
                            width=8,text="Print",command=iPrint).grid(row=0,column=2,padx=1)
        self.btnDisplay=Button(TopFrame1,pady=1,bd=4,fg="black",font=('arial',16,'bold'),padx=24,bg='dodger blue',
                            width=8,text="Display",command=DisplayData).grid(row=0,column=3,padx=1)
        self.btnUpdate=Button(TopFrame1,pady=1,bd=4,fg="black",font=('arial',16,'bold'),padx=24,bg='dodger blue',
                            width=8,text="Update",command=update).grid(row=0,column=4,padx=1)
        self.btnDelete=Button(TopFrame1,pady=1,bd=4,fg="black",font=('arial',16,'bold'),padx=24,bg='dodger blue',
                            width=8,text="Delete",command=DeleteData).grid(row=0,column=5,padx=1)
        self.btnSearch=Button(TopFrame1,pady=1,bd=4,fg="black",font=('arial',16,'bold'),padx=24,bg='dodger blue',
                            width=8,text="Search",command=SearchData).grid(row=0,column=6,padx=1)
        self.btnReset=Button(TopFrame1,pady=1,bd=4,fg="black",font=('arial',16,'bold'),padx=24,bg='dodger blue',
                            width=8,text="Reset",command=Reset).grid(row=0,column=7,padx=1)
        self.btnExit=Button(TopFrame1,pady=1,bd=4,fg="black",font=('arial',16,'bold'),padx=24,bg='dodger blue',
                            width=8,text="Exit",command = iQuit).grid(row=0,column=8,padx=1)

root=Tk()
obj = Employee(root)
root.mainloop()
