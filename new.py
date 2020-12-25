from tkinter import*
from tkinter import ttk
import random
from tkinter import messagebox
from datetime import datetime
import time;
import tempfile,os
import sqlite3
import newEmployeeDatabase
from tkinter import BOTH, END, LEFT


root = Tk()
root.title("Employee Database Management System")
root.geometry("1353x740+0+0")
root.configure (bg = 'gainsboro')


Ed = StringVar()
Firstname =StringVar()
Surname =StringVar()
Middlename =StringVar()
Address =StringVar()
Department =StringVar()
DOB =StringVar()
CityWeighting = DoubleVar()
Mobile =StringVar()
Email =StringVar()
BasicSalary=DoubleVar()
OverTime=DoubleVar()
GrossPay=StringVar()
NetPay=StringVar()
Tax=StringVar()
Pension=StringVar()
stdloan = StringVar()
NIPayment=StringVar()
Deductions=StringVar()
Gender=StringVar()
Payday=StringVar()
TaxPeriod=StringVar()
NINumber=StringVar()
NICode=StringVar()
TaxablePay=StringVar()
PensionablePay=StringVar()
OtherPaymentDue=DoubleVar()
TaxCode=StringVar()
ReferenceNo=StringVar()
OtherPaymentDue.set(0.00)
EmpNo=StringVar()




#===========================================FRAMES AND BORDERS==============================================================================================================
TopFrame1 = Frame(root, bd = 10,width =1353, height = 50,bg='gainsboro',relief= GROOVE)
TopFrame1.pack(fill=X)

lblTitle= Label(TopFrame1,font=('times new roman',20,'bold'),text="\t\t\t\tEMPLOYEE DATABASE MANAGEMENT SYSTEM",bd=7,bg='gainsboro',anchor='w',pady=2)
lblTitle.pack(fill=X)

TopFrame2 = Frame(root, bd = 10,width =1353, height = 500,bg='gainsboro',relief= GROOVE)
TopFrame2.pack(fill=X)

TopFrame3 = Frame(root, bd = 10,width =1353, height = 200,bg='gainsboro',relief= GROOVE)#
TopFrame3.pack(fill=X)

TopFrame4 = Frame(root, bd = 10,width =1353, height = 100,bg='gainsboro',relief= GROOVE)  #buttons
TopFrame4.pack(fill=X)

LeftFrame1 = Frame(TopFrame1,bd=10, width = 550,height=500,padx=4,pady=4,bg='gainsboro',relief=GROOVE)  #employee info frame
LeftFrame1.pack(side=LEFT)

LeftFrame2 = Frame(TopFrame1,bd=10, width = 550,height=500,padx=4,pady=4,bg='gainsboro',relief=GROOVE)   #employee payment frame
LeftFrame2.pack(side=LEFT)

LeftFrame3 = Frame(TopFrame1,bd=10, width = 500,height=500,padx=4,pady=4,bg='gainsboro',relief=GROOVE)  #receipt frame
LeftFrame3.pack(side=RIGHT)

txtReceipt = Text(LeftFrame3,height=25,width=45,bd=10,font=('times new roman',12,'bold'))
txtReceipt.pack(fill=X)

lbLabel = Label(TopFrame2, font=('arial',10,'bold'),padx=6,pady=2,bg='gainsboro',
text = "Reference\tFirstname\tSurname\tAddress\t\tGender\t\tMobileNo.\tE-Mail\tNINumber\tStudent Loan\t\tTax\tPension\t\tDeductions\tNet Pay\t\tGrossPay")
lbLabel.grid(row = 0,column =0,columnspan = 17)
#===================================================VARIABLES=======================================================================================================

        # global Ed
        # Firstname =StringVar()
        # Surname =StringVar()
        # MiddleName =StringVar()
        # Address =StringVar()
        # Department =StringVar()
        # DOB =StringVar()
        # CityWeighting = IntVar()
        # Mobile =StringVar()
        # Email =StringVar()
        # BasicSalary=IntVar()
        # OverTime=StringVar()
        # GrossPay=StringVar()
def EmployeeRec(event):
    # searchEd = lstEmployee.curselection()[0]
    # Ed = lstEmployee.get(searchEd)
    no=lstEmployee.get()
    c.execute("SELECT * FROM EMPLOYEE WHERE ReferenceNo = ?",(no,))
    rows=c.fetchall()
    for i in rows:
        print(i)
        Firstname.set(i[1])
        Middlename.set(i[2])
        Surname.set(i[3])
        DOB.set(i[4])
        Address.set(i[5])
        Gender.set(i[6])
        Email.set(i[7])
        Mobile.set(i[8])
        Department.set(i[9])

        c.execute("SELECT * FROM EMP_PAYMENT WHERE ID = ?",(no,))
        r=c.fetchall()
        print(r)
        for i in r:
          CityWeighting.set(i[1])
          BasicSalary.set(i[2])
          OverTime.set(i[3])
          OtherPaymentDue.set(i[4])

    c.execute("SELECT * FROM EMP_PAY_ID WHERE ID = ?",(no,))
    r=c.fetchall()
    print(r)
    for i in r:
      NIPayment.set(i[1])
      NICode.set(i[2])
      NINumber.set(i[3])
      TaxCode.set(i[4])
      Payday.set(i[5])

    c.execute("SELECT * FROM EMP_EXPENSE WHERE ID = ?",(no,))
    r=c.fetchall()
    print(r)
    for i in r:
        PensionablePay.set(i[1])
        TaxablePay.set(i[2])
        Deductions.set(i[3])
        stdloan.set(i[4])
        Pension.set(i[5])

    c.execute("SELECT * FROM EMP_UNIQUE_ID WHERE ID = ?",(no,))
    r=c.fetchall()
    print(r)
    for i in r:
      NetPay.set(i[1])
      GrossPay.set(i[2])
      EmpNo.set(i[3])
      TaxPeriod.set(i[4])

        # NetPay=StringVar()
        # Tax=StringVar()
        # Pension=StringVar()
        # StudentLoan = StringVar()
        # NIPayment=StringVar()
        # Deductions=StringVar()
def MonthlySalary():
    print("hhugjhvv")
    PayRef()
        # Gender=StringVar()
def iPrint():
    q=txtReceipt.get("1.0","end-1c")
    filename=tempfile.mktemp(".doc")
    open (filename, "w").write(q)
    os.startfile(filename, "print")
        # Payday=StringVar()
def DisplayData():

    lstEmployee.delete(0,END)
    for row in newEmployeeDatabase.viewData():
        lstEmployee.insert(END,row,str(""))
        # TaxPeriod=StringVar()
def update():
    if(len(ReferenceNo.get())!=0):
        newEmployeeDatabase.deleteRec(Ed[0])
    if(len(ReferenceNo.get())!=0):
        newEmployeeDatabase.addEmployeeRec(ReferenceNo.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),NINumber.get(),stdloan.get(),Tax.get(),Pension.get(),Deductions.get(),NetPay.get(),GrossPay.get())
        lstEmployee.delete(0,END)
        lstEmployee.insert(END,(ReferenceNo.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(), Mobile.get(),
        NINumber.get(),stdloan.get(),Tax.get(),Pension.get(),Deductions.get(),NetPay.get(),GrossPay.get()))
        # NINumber=StringVar()
        # NICode=StringVar()
        # TaxablePay=StringVar()
        # PensionablePay=StringVar()
        # OtherPaymentDue=StringVar()
        # TaxCode=StringVar()
        # ReferenceNo=StringVar()
        # OtherPaymentDue.set("0.00")
        # EmpNo=StringVar()
def addData ():
    if(len(ReferenceNo.get())!=0):
        newEmployeeDatabase.addEmployeeRec(ReferenceNo.get(),Firstname.get(),Middlename.get(),Surname.get(),DOB.get(),Address.get(),Gender.get(),
        Email.get(),Mobile.get(),Department.get(),CityWeighting.get(),BasicSalary.get(),OverTime.get(),OtherPaymentDue.get())
        lstEmployee.delete(0,END)
        lstEmployee.insert(END,(ReferenceNo.get(),Firstname.get(),Middlename.get(),Surname.get(),DOB.get(),Address.get(),Gender.get(),
        Email.get(),Mobile.get(),Department.get(),CityWeighting.get(),BasicSalary.get(),OverTime.get(),OtherPaymentDue.get()))


conn=sqlite3.connect("newEmployee.db")
c = conn.cursor()
c.execute(''' SELECT ReferenceNo FROM EMPLOYEE''')
ids=c.fetchall()



def DeleteData():
    if(len(ReferenceNo.get())!=0):
        newEmployeeDatabase.deleteRec(Ed[0])
        ClearData()
        DisplayData()
#Reference,Firstname,Middlename,Surname,DOB,Adress,Gender,Email,Mobile,Department,CityWeighting,BasicSalary,OverTime,OtherPaymentDue,Payday,TaxPeriod,NINumber,stdLoan,Tax,Pension,Deductions,NetPay,GrossPay,NICode,AadharCardNo,PANCardNo
def SearchData():
    lstEmployee.delete(0,END)
    for row in newEmployeeDatabase.searchData(ReferenceNo.get(),Firstname.get(),Middlename.get(),Surname.get(),DOB.get(),Address.get(),Gender.get(),
        Email.get(),Mobile.get(),Department.get(),CityWeighting.get(),BasicSalary.get(),OverTime.get(),OtherPaymentDue.get(),Payday.get(),TaxPeriod.get(),
        NINumber.get(),stdloan.get(),Tax.get(),Pension.get(),Deductions.get(),NetPay.get(),GrossPay.get(),NIPayment.get(),NICode.get()):
        lstEmployee.insert(END,row,str(""))



def iExit():
    iExit = messagebox.askyesno("BILLING SYSTEM", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def ClearData():


    ReferenceNo.delete(0 ,END)
    Firstname.delete(0, END)
    Middlename.delete(0, END)

    Surname.delete(0, END)
    DOB.delete(0, END)
    Address.delete(0, END)
    Gender.delete(0, END)
    Email.delete(0, END)
    Mobile.delete(0, END)

    Department.delete(0, END)
    CityWeighting.delete(0, END)
    BasicSalary.delete(0, END)
    OverTime.delete(0, END)
    OtherPaymentDue.delete(0, END)
    Payday.delete(0, END)

    TaxPeriod.delete(0, END)
    Pension.delete(0, END)
    stdloan.delete(0, END)
    Deductions.delete(0, END)
    NIPayment.delete(0, END)
    NICode.delete(0, END)

    NINumber.delete(0,END)
    TaxablePay.delete(0,END)
    PensionablePay.delete(0,END)
    TaxCode.delete(0,END)
    NetPay.delete(0,END)
    GrossPay.delete(0,END)
    txtReceipt.delete('1.0',END)


def PayRef():
   Payday.set(time.strftime("%d/%m/%Y"))
   Refpay = random.randint(16462,708488)
   Refpaid = ("Ref" + str(Refpay))
   ReferenceNo.set(Refpaid)

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
   stdloan.set(MM_stdLoan)
   M_NIPayment = ((BS + CW + OT + OPD) * 0.011)
   MM_NIPayment = "$", str('%.2f'%(M_NIPayment))
   stdloan.set(MM_NIPayment)
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

   txtReceipt.insert(END,'\t\t Monthly Pay Slip' + "\n\n")
   txtReceipt.insert(END,'ReferenceNo:\t\t\t' + ReferenceNo.get() +"\n")
   txtReceipt.insert(END,'Payday:\t\t\t' + Payday.get() + "\n")
   txtReceipt.insert(END,'Employee Firstname :\t\t\t' + Firstname.get() + "\n")
   txtReceipt.insert(END,'Employee Surname:\t\t\t' + Surname.get() + "\n")
   txtReceipt.insert(END,'Tax:\t\t\t' + Tax.get() + "\n")
   txtReceipt.insert(END,'Pension:\t\t\t' + Pension.get() + "\n")
   txtReceipt.insert(END,'Student Loan:\t\t\t' + stdloan.get() + "\n")
   txtReceipt.insert(END,'NI Number:\t\t\t' + NINumber.get() + "\n")
   txtReceipt.insert(END,'NI Payment:\t\t\t' + NIPayment.get() + "\n")
   txtReceipt.insert(END,'Deductions:\t\t\t' + Deductions.get() + "\n")
   txtReceipt.insert(END,'City Weighting:\t\t\t' + str('$ %.2f'%(CityWeighting.get())) + "\n")
   txtReceipt.insert(END,'Tax Paid:\t\t\t' + str('$ %.2f'%(BasicSalary.get())) + "\n")
   txtReceipt.insert(END,'OverTime:\t\t\t' + "$" + OverTime.get() +  "\n")
   txtReceipt.insert(END,'NetPay:\t\t\t' + NetPay.get() + "\n")
   txtReceipt.insert(END,'City Weighting:\t\t\t' + GrossPay.get() + "\n")

   addData()
def insert():
  newEmployeeDatabase.insert(ReferenceNo.get(),Firstname.get(),Middlename.get(),Surname.get(),DOB.get(),Address.get(),Gender.get(),Email.get(),Mobile.get(),
  Department.get(),CityWeighting.get(),BasicSalary.get(),OverTime.get(),OtherPaymentDue.get(),Payday.get(),TaxPeriod.get(),Pension.get(),
  stdloan.get(),Deductions.get(),NIPayment.get(),NICode.get(),NINumber.get(),TaxablePay.get(),PensionablePay.get(),TaxCode.get(),NetPay.get(),GrossPay.get(),EmpNo.get())
  return

#==================================================RECEIPT AND SCROLLBAR===========================================================================================
scrollbar = Scrollbar(TopFrame2)
scrollbar.grid(row=1,column=1,sticky='ns')

lstEmployee = Listbox(TopFrame2, width = 165,height=5,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
lstEmployee.bind('<<ListboxSelected>>',EmployeeRec)
lstEmployee.grid(row=1,column=0,padx=1,sticky='nsew')
scrollbar.config(command = lstEmployee.xview)

lblReference= Label(LeftFrame1,font=('arial',12,'bold'),text="ReferrenceNo",bd=7,bg='gainsboro',anchor='w')
lblReference.grid(row=0,column=0,sticky=W,padx=5)
txtReference= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=ReferenceNo)
txtReference.grid(row=0,column=1)

lblFirstname= Label(LeftFrame1,font=('arial',12,'bold'),text="Firstname",bd=7,bg='gainsboro',anchor='w')
lblFirstname.grid(row=1,column=0,sticky=W,padx=5)
txtFirstname= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Firstname)
txtFirstname.grid(row=1,column=1)

lblMiddlename= Label(LeftFrame1,font=('arial',12,'bold'),text="Middlename",bd=7,bg='gainsboro', justify='left')
lblMiddlename.grid(row=2,column=0,sticky=W,padx=5)
txtMiddlename= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Middlename)
txtMiddlename.grid(row=2,column=1)

lblSurname= Label(LeftFrame1,font=('arial',12,'bold'),text="Surname",bd=7,bg='gainsboro', justify='left')
lblSurname.grid(row=3,column=0,sticky=W,padx=5)
txtSurname= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Surname)
txtSurname.grid(row=3,column=1)

lblDOB= Label(LeftFrame1,font=('arial',12,'bold'),text="DOB",bd=7,bg='gainsboro', justify='left')
lblDOB.grid(row=4,column=0,sticky=W,padx=5)
txtDOB= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=DOB)
txtDOB.grid(row=4,column=1)

lblAddress= Label(LeftFrame1,font=('arial',12,'bold'),text="Address",bd=7,bg='gainsboro')
lblAddress.grid(row=5,column=0,sticky=W,padx=5)
txtAddress= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Address)
txtAddress.grid(row=5,column=1)

lblGender= Label(LeftFrame1,font=('arial',12,'bold'),text="Gender",bd=7,bg='gainsboro')
lblGender.grid(row=6,column=0,sticky=W,padx=5)
txtGender= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Gender)
txtGender.grid(row=6,column=1)

lblEMail= Label(LeftFrame1,font=('arial',12,'bold'),text="E-Mail",bd=7,bg='gainsboro')
lblEMail.grid(row=7,column=0,sticky=W,padx=5)
txtEMail= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Email)
txtEMail.grid(row=7,column=1)

lblMobile= Label(LeftFrame1,font=('arial',12,'bold'),text="Mobile",bd=7,bg='gainsboro')
lblMobile.grid(row=8,column=0,sticky=W,padx=5)
txtMobile= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Mobile)
txtMobile.grid(row=8,column=1)

lblDepartment= Label(LeftFrame1,font=('arial',12,'bold'),text="Department",bd=7,bg='gainsboro')
lblDepartment.grid(row=9,column=0,sticky=W,padx=5)
txtDepartment= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Department)
txtDepartment.grid(row=9,column=1)

lblCityWeighting= Label(LeftFrame1,font=('arial',12,'bold'),text="CityWeighting",bd=7,bg='gainsboro')
lblCityWeighting.grid(row=10,column=0,sticky=W,padx=5)
txtCityWeighting= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=CityWeighting)
txtCityWeighting.grid(row=10,column=1)

lblBasicSalary= Label(LeftFrame1,font=('arial',12,'bold'),text="BasicSalary",bd=7,bg='gainsboro')
lblBasicSalary.grid(row=11,column=0,sticky=W,padx=5)
txtBasicSalary= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=BasicSalary)
txtBasicSalary.grid(row=11,column=1)

lblOverTime= Label(LeftFrame1,font=('arial',12,'bold'),text="OverTime",bd=7,bg='gainsboro')
lblOverTime.grid(row=12,column=0,sticky=W,padx=5)
txtOverTime= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=OverTime)
txtOverTime.grid(row=12,column=1)

lblOtherPaymentDue= Label(LeftFrame1,font=('arial',12,'bold'),text="Other Payment Due",bd=7,bg="gainsboro",anchor='w',justify='left')
lblOtherPaymentDue.grid(row=13,column=0,sticky=W,padx=5)
txtOtherPaymentDue= Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=OtherPaymentDue)
txtOtherPaymentDue.grid(row=13,column=1)

lblPayday= Label(LeftFrame2,font=('arial',12,'bold'),text="Payday",bd=7,bg="gainsboro",anchor='w',justify='left')
lblPayday.grid(row=0,column=0,sticky=W,padx=5)
txtPayday= Entry(LeftFrame2,font=('arial',12,'bold'),bd=5,width=30, justify='left',textvariable=Payday)
txtPayday.grid(row=0,column=1)

lblTaxPeriod= Label(LeftFrame2,font=('arial',12,'bold'),text="TaxPeriod",bd=7,bg="gainsboro",anchor='w',justify='left')
lblTaxPeriod.grid(row=1,column=0,sticky=W,padx=5)
txtTaxPeriod= Entry(LeftFrame2,font=('arial',12,'bold'),bd=5,width=30, justify='left',textvariable=TaxPeriod)
txtTaxPeriod.grid(row=1,column=1)

lblPension= Label(LeftFrame2,font=('arial',12,'bold'),text="Pension",bd=7,bg="gainsboro",anchor='w',justify='left')
lblPension.grid(row=2,column=0,sticky=W,padx=5)
txtPension= Entry(LeftFrame2,font=('arial',12,'bold'),bd=5,width=30, justify='left',textvariable=Pension)
txtPension.grid(row=2,column=1)

lblStudentLoan= Label(LeftFrame2,font=('arial',12,'bold'),text="StudentLoan",bd=7,bg="gainsboro",anchor='w',justify='left')
lblStudentLoan.grid(row=3,column=0,sticky=W,padx=5)
txtStudentLoan= Entry(LeftFrame2,font=('arial',12,'bold'),bd=5,width=30, justify='left',textvariable=stdloan)
txtStudentLoan.grid(row=3,column=1)

lblDeductions= Label(LeftFrame2,font=('arial',12,'bold'),text="Deductions",bd=7,bg="gainsboro",anchor='w',justify='left')
lblDeductions.grid(row=4,column=0,sticky=W,padx=5)
txtDeductions= Entry(LeftFrame2,font=('arial',12,'bold'),bd=5,width=30, justify='left',textvariable=Deductions)
txtDeductions.grid(row=4,column=1)

lblNIPayment= Label(LeftFrame2,font=('arial',12,'bold'),text="NIPayment",bd=7,bg="gainsboro",anchor='w',justify='left')
lblNIPayment.grid(row=5,column=0,sticky=W,padx=5)
txtNIPayment= Entry(LeftFrame2,font=('arial',12,'bold'),bd=5,width=30, justify='left',textvariable=NIPayment)
txtNIPayment.grid(row=5,column=1)

lblNICode= Label(LeftFrame2,font=('arial',12,'bold'),text="NICode",bd=7,bg="gainsboro",anchor='w',justify='left')
lblNICode.grid(row=6,column=0,sticky=W,padx=5)
txtNICode= Entry(LeftFrame2,font=('arial',12,'bold'),bd=5,width=30, justify='left',textvariable=NICode)
txtNICode.grid(row=6,column=1)

lblNINumber= Label(LeftFrame2,font=('arial',12,'bold'),text="NINumber",bd=7,bg="gainsboro",anchor='w',justify='left')
lblNINumber.grid(row=7,column=0,sticky=W,padx=5)
txtNINumber= Entry(LeftFrame2,font=('arial',12,'bold'),bd=5,width=30, justify='left',textvariable=NINumber)
txtNINumber.grid(row=7,column=1)

lblTaxablePay= Label(LeftFrame2,font=('arial',12,'bold'),text="TaxablePay",bd=7,bg="gainsboro",anchor='w',justify='left')
lblTaxablePay.grid(row=8,column=0,sticky=W,padx=5)
txtTaxablePay= Entry(LeftFrame2,font=('arial',12,'bold'),bd=5,width=30, justify='left',textvariable=TaxablePay)
txtTaxablePay.grid(row=8,column=1)

lblPensionablePay= Label(LeftFrame2,font=('arial',12,'bold'),text="PensionablePay",bd=7,bg="gainsboro",anchor='w',justify='left')
lblPensionablePay.grid(row=9,column=0,sticky=W,padx=5)
txtPensionablePay= Entry(LeftFrame2,font=('arial',12,'bold'),bd=5,width=30, justify='left',textvariable=PensionablePay)
txtPensionablePay.grid(row=9,column=1)

lblTaxCode= Label(LeftFrame2,font=('arial',12,'bold'),text="TaxCode",bd=7,bg="gainsboro",anchor='w',justify='left')
lblTaxCode.grid(row=10,column=0,sticky=W,padx=5)
txtTaxCode= Entry(LeftFrame2,font=('arial',12,'bold'),bd=5,width=30, justify='left',textvariable=TaxCode)
txtTaxCode.grid(row=10,column=1)

lblNetPay= Label(LeftFrame2,font=('arial',12,'bold'),text="NetPay",bd=7,bg="gainsboro",anchor='w',justify='left')
lblNetPay.grid(row=11,column=0,sticky=W,padx=5)
txtNetPay= Entry(LeftFrame2,font=('arial',12,'bold'),bd=5,width=30, justify='left',textvariable=NetPay)
txtNetPay.grid(row=11,column=1)

lblGrossPay= Label(LeftFrame2,font=('arial',12,'bold'),text="GrossPay",bd=7,bg="gainsboro",anchor='w',justify='left')
lblGrossPay.grid(row=12,column=0,sticky=W,padx=5)
txtGrossPay= Entry(LeftFrame2,font=('arial',12,'bold'),bd=5,width=30, justify='left',textvariable=GrossPay)
txtGrossPay.grid(row=12,column=1)

lblEmpNo= Label(LeftFrame2,font=('arial',12,'bold'),text="EMPNo",bd=7,bg="gainsboro",anchor='w',justify='left')
lblEmpNo.grid(row=13,column=0,sticky=W,padx=5)
txtEmpNo= Entry(LeftFrame2,font=('arial',12,'bold'),bd=5,width=30, justify='left',textvariable=EmpNo)
txtEmpNo.grid(row=13,column=1)

#======================================BUTTONS FRAMES============================================================================================================
btnAddNewTotal=Button(TopFrame3,pady=2,bd=4,fg="black",font=('arial',16,'bold'),padx=24,bg='gainsboro',
                    width=10,text="AddNew/Total",command=MonthlySalary).grid(row=0,column=1,padx=1)
btnPrint=Button(TopFrame3,pady=2,bd=4,fg="black",font=('arial',16,'bold'),padx=24,bg='gainsboro',
                    width=10,text="Print",command=iPrint).grid(row=0,column=2,padx=1)
btnDisplay=Button(TopFrame3,pady=2,bd=4,fg="black",font=('arial',16,'bold'),padx=24,bg='gainsboro',
                    width=10,text="Display",command=DisplayData).grid(row=0,column=3,padx=1)
btnUpdate=Button(TopFrame3,pady=2,bd=4,fg="black",font=('arial',16,'bold'),padx=24,bg='gainsboro',
                    width=10,text="Update",command=update).grid(row=0,column=4,padx=1)
btnDelete=Button(TopFrame3,pady=2,bd=4,fg="black",font=('arial',16,'bold'),padx=24,bg='gainsboro',
                    width=10,text="Delete",command=DeleteData).grid(row=0,column=5,padx=1)
btnSearch=Button(TopFrame3,pady=2,bd=4,fg="black",font=('arial',16,'bold'),padx=24,bg='gainsboro',
                    width=10,text="Search",command=SearchData).grid(row=0,column=6,padx=1)
btnReset=Button(TopFrame3,pady=2,bd=4,fg="black",font=('arial',16,'bold'),padx=24,bg='gainsboro',
                    width=10,text="ClearData").grid(row=0,column=7,padx=1)
btnExit=Button(TopFrame3,pady=2,bd=4,fg="black",font=('arial',16,'bold'),padx=24,bg='gainsboro',
                    width=8,text="Exit",command = iExit).grid(row=0,column=8,padx=1)


root.mainloop()
