#newEmployeeDatabase(2)
import sqlite3

def main():
    conn=sqlite3.connect("newEmployee.db")
    c = conn.cursor()

    c.execute('''PRAGMA foreign_keys = ON''')

    c.execute(''' CREATE TABLE IF NOT EXISTS EMPLOYEE(
            ReferenceNo VARCHAR(15) PRIMARY KEY,
            Firstname VARCHAR(15),
            Middlename VARCHAR(15),
            Surname VARCHAR(15),
            DOB INTEGER,
            Address VARCHAR(15),
            Gender VARCHAR(15),
            Email VARCHAR(15),
            Mobile INTEGER,
            Department VARCHAR(15))''')

    c.execute(''' CREATE TABLE IF NOT EXISTS  EMP_PAYMENT(
            ID PRIMARY KEY REFERENCES EMPLOYEE(ReferenceNo) ON DELETE CASCADE,
            CityWeighting VARCHAR(15) ,
            BasicSalary VARCHAR(15),
            OverTime VARCHAR(15),
            OtherPaymentDue VARCHAR(15)) ''')


    c.execute(''' CREATE TABLE IF NOT EXISTS EMP_PAY_ID(
            ID INTEGER PRIMARY KEY REFERENCES EMPLOYEE(ReferenceNo) ON DELETE CASCADE,
            NIPayment VARCHAR2(15),
            NICode VARCHAR(15),
            NINumber VARCHAR(15),
            TaxCode VARCHAR(15),
            Payday VARCHAR(15))''')

    c.execute(''' CREATE TABLE IF NOT EXISTS EMP_EXPENSE(
            ID INTEGER PRIMARY KEY REFERENCES EMPLOYEE(ReferenceNo) ON DELETE CASCADE,
            PensionablePay VARCHAR(15),
            TaxablePay VARCHAR(15),
            Deductions VARCHAR(15),
            StdLoan VARCHAR(15),
            Pension VARCHAR(15))''')

    c.execute(''' CREATE TABLE IF NOT EXISTS EMP_UNIQUE_ID(
            ID INTEGER PRIMARY KEY REFERENCES EMPLOYEE(ReferenceNo) ON DELETE CASCADE,
            NetPay VARCHAR(15),
            GrossPay VARCHAR(15),
            EmpNo VARCHAR(15),
            TaxPeriod VARCHAR(15))''')

    conn.commit()
    conn.close()


main()

def insert(ReferenceNo,Firstname,Middlename,DOB,Address,Gender,Email,Mobile,Department,CityWeighting,BasicSalary,OverTime,OtherPaymentDue,NIPayment,NICode,NINumber,TaxCode,Payday,
            PensionablePay,TaxablePay,Deductions,StdLoan,Pension,NetPay,GrossPay,EmpNo,TaxPeriod):
    #print(t)
    conn=sqlite3.connect('newEmployee.db')
    c=conn.cursor()
    c.execute('''PRAGMA foreign_keys = ON''')
    c.execute("INSERT INTO EMPLOYEE (ReferenceNo,Firstname,Middlename,DOB,Address,Gender,Email,Mobile,Department) VALUES(?,?,?,?,?,?,?,?,?)",(ReferenceNo,Firstname,Middlename,DOB,Address,Gender,Email,Mobile,Department))
    c.execute("INSERT INTO EMP_PAYMENT (ID,CityWeighting,BasicSalary,OverTime,OtherPaymentDue) VALUES (?,?,?,?,?)",(ReferenceNo,CityWeighting,BasicSalary,OverTime,OtherPaymentDue))
    c.execute("Insert INTO EMP_PAY_ID (ID,NIPayment,NICode,NINumber,TaxCode,Payday) VALUES (?,?,?,?,?,?)",(ReferenceNo,NIPayment,NICode,NINumber,TaxCode,Payday))
    c.execute("Insert INTO  EMP_EXPENSE (ID,PensionablePay,TaxablePay,Deductions,StdLoan,Pension) VALUES(?,?,?,?,?,?)",(ReferenceNo,PensionablePay,TaxablePay,Deductions,StdLoan,Pension))
    c.execute("Insert INTO EMP_UNIQUE_ID (ID,NetPay,GrossPay,EmpNo,TaxPeriod) VALUES(?,?,?,?,?)",(ReferenceNo,NetPay,GrossPay,EmpNo,TaxPeriod))
    conn.commit()
    conn.close()


def delete(b):
    conn=sqlite3.connect('newEmployee.db')
    c=conn.cursor()
    c.execute('''PRAGMA foreign_keys = ON''')
    c.execute("DELETE FROM EMPLOYEE WHERE ReferenceNo=(?) ",(b,))
    conn.commit()
    conn.close()



def Searchdata(ReferenceNo,Firstname,Middlename,Mobile):


    conn=sqlite3.connect('newEmployee.db')
    c=conn.cursor()
    c.execute ("SELECT * FROM EMPLOYEE WHERE ReferenceNo =? OR Firstname =? OR Middlename=? OR Mobile=?" ,(ReferenceNo,Firstname,Middlename,Mobile))
    row = c.fetchone()
    c.execute ("SELECT * FROM EMP_PAYMENT WHERE ID=(SELECT ReferenceNo FROM EMPLOYEE WHERE Firstname=? OR Middlename=? OR Mobile=?)",(ReferenceNo,Firstname,Middlename,Mobile))

    row2= c.fetchone()
    c.execute ("SELECT * FROM EMP_PAY_ID WHERE ID=(SELECT ReferenceNo FROM EMPLOYEE WHERE Firstname=? OR Middlename=? OR Mobile=?)",(ReferenceNo,Firstname,Middlename,Mobile))
    row3 = c.fetchone()
    c.execute ("SELECT * FROM EMP_EXPENSE WHERE ID=(SELECT ReferenceNo FROM EMPLOYEE WHERE Firstname=? OR Middlename=? OR Mobile=?)",(ReferenceNo,Firstname,Middlename,Mobile))
    row4 = c.fetchone()
    c.execute ("SELECT * FROM EMP_UNIQUE_ID WHERE ID=(SELECT ReferenceNo FROM EMPLOYEE WHERE Firstname=? OR Middlename=? OR Mobile=?)",(ReferenceNo,Firstname,Middlename,Mobile))
    row5 = c.fetchone()
    conn.commit()
    conn.close()

    return row,row2,row3,row4,row5
