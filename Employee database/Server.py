import sqlite3

#creating table of data declaring ID as primary key
def create_table():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS employees (
                    employeeId TEXT PRIMARY KEY,
                    employeename TEXT,
                    employeeExp TEXT,
                    employeeAge TEXT,
                    employeePos TEXT,
                    employeeRole TEXT,
                    employeePerf TEXT,
                    employeePay TEXT,
                    employeeStrt TEXT,
                    employeeEnd TEXT)''')
                    
                

    conn.commit()
    conn.close()
    
#grabs data to then use in main programn
def grabdata():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    conn.close()
    return employees
    
#add data function
def adddata(employeeId, employeename,employeeExp, employeeAge, employeePos, employeeRole,employeePerf,employeePay,employeeStrt,employeeEnd):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO employees (employeeId, employeename,employeeExp, employeeAge, employeePos, employeeRole,employeePerf,employeePay,employeeStrt,employeeEnd) VALUES (?,?,?,?,?,?,?,?,?,?)',
                   (employeeId, employeename,employeeExp, employeeAge, employeePos, employeeRole,employeePerf,employeePay,employeeStrt,employeeEnd))
    conn.commit()
    conn.close()
        
#update data function
def updatedata(employeeId, Newemployeename,NewemployeeExp, NewemployeeAge, NewemployeePos, NewemployeeRole,NewemployeePerf,NewemployeePay,NewemployeeStrt,NewemployeeEnd):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    #SQL command to update data in database
    cursor.execute('UPDATE employees SET  employeename = ?,employeeExp = ?, employeeAge = ?, employeePos = ?, employeeRole = ?,employeePerf = ?,employeePay = ?,employeeStrt = ?,employeeEnd = ?', 
                   (Newemployeename,NewemployeeExp, NewemployeeAge, NewemployeePos, NewemployeeRole,NewemployeePerf,NewemployeePay,NewemployeeStrt,NewemployeeEnd))
    conn.commit()
    conn.close()
    
#delete function
def deldata(employeeid):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE employeeid = ?',(str(employeeid),))
    conn.commit()
    conn.close()
        
#checks if employee id exists
def datacheck(employeeid):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM employees WHERE employeeid = ?',(str(employeeid),))
    result = cursor.fetchone()
    conn.close()
    return result [0] > 0

create_table()