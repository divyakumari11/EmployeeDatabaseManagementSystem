import sqlite3
#BackendB

def EmployeeData():
       con=sqlite3. connect ("Employee. db")
       cur=con.cursor ()
       cur.execute ("CREATE TABLE IF NOT EXISTS Employee (id INTEGER PRIMARY KEY, Reference text,\
       Firstname text,Surname text, Address text, Gender text, Mobile text, NINumber text, \
       stdLoan text, Tax text, Pension text, Deductions text, NetPay text, GrossPay text)")
       con.commit()
       con.close()

def addEmployeeRec (Reference,Firstname, Surname, Adress, Gender, Mobile,NINumber,stdLoan, Tax, Pension, Deductions, NetPay , GrossPay):
       con = sqlite3.connect("Employee.db")
       cur=con.cursor()
       cur.execute("INSERT INTO Employee VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,? )",\
                   (Reference,Firstname, Surname, Adress, Gender, Mobile,NINumber,stdLoan, Tax, Pension, Deductions, NetPay , GrossPay))
       con.commit()
       con.close()

def viewData():
       con= sqlite3. connect ("Employee.db")
       cur = con.cursor()
       cur.execute ("SELECT * FROM Employee")
       rows = cur.fetchall()
       con.close()
       return Rows

def deleteRec(id):
       con=sqlite3. connect ("Employee.db ")
       cur=con.cursor()
       cur.execute ("DELETE*FROM Employee WHERE id=?",(id))
       con.commit ()
       con.close()

def searchData(Reference ="",Firstname ="",Surname="", Adress="", Gender="", Mobile="",NINumber="",stdLoan="", Tax="", \
                Pension="", Deductions="", NetPay="" , GrossPay=""):
      con=sqlite3.connect ("Employee.db")
      cur=con.cursor()
      cur.execute ("SELECT * FROM Employee WHERE Reference =? OR Firstname=? OR Surname=? OR Adress=? OR Gender=? OR Mobile=?  \
                    OR NINumber=? OR stdLoan=? OR Tax=? OR Pension=? OR Deductions=? OR NetPay =?OR GrossPay=?\
               (Reference,Firstname,Surname,Adress,Gender,Mobile,NINumber,stdLoan,Tax,Pension,Deductions,NetPay,GrossPay)")
      rows=cur.fetchall()
      con.close()
      return Rows

def dataUpdate(Reference =" ",Firstname =" ",Surname=" ", Adress=" ", Gender=" ", Mobile=" ",NINumber=" ",stdLoan=" ", Tax=" ", Pension=" ", Deductions=" ", NetPay=" " , GrossPay=" "):
      con=sqlite3. connect ("Employee.db")
      cur=con.cursor ( )
      cur.execute ("UPDATE Employee SET Reference =?,Firstname=?,Surname=?, Adress=?, Gender=?,Mobile=?\, NINumber=?, stdLoan=?, Tax=? , Pension=? ,Deductions=?,NetPay =?, GrossPay=?",\
                          (Reference,Firstname, Surname, Adress, Gender, Mobile,NINumber,stdLoan, Tax, Pension, Deductions, NetPay , GrossPay,id))
      rows=cur.fetchall ( )
      con.close( )
      return Rows
EmployeeData()
