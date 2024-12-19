


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import Server



class Main:


    
        
        
        
        
        
        
      

    
    def loginvalidation(self):
        print("Username recieved: ", self.user.get())
        print("password recieved: ", self.password.get())
        if self.user.get() == "25369245" and self.password.get() == "Kyle":
            success = Toplevel(self.master)
            success.geometry("200x75")


            #delay for success window to close
            success.after(3000, lambda Tk= success:[Tk.destroy()])
            successLabel = Label(success, text="Login is successful").grid(row=0, column=0)







            print("Login is successful")
            #wait until success window is closed to open new page
            self.master.wait_window(success)
            self.master.destroy()
            self.Newwindow()

        else:
            # wrong login screen
            fail = Tk()
            fail.geometry("200x75")

            fail.after(3000, lambda Tk = fail:[Tk.destroy()])
            failLabel = Label(fail, text="Your account is locked").grid(row=0, column=0)
            print("Your account is locked")
        return
    def __init__(self, master):
        self.master = master

        # window

        self.master.geometry('500x175')
        self.master.title('Admin Login')
        self.master.configure(bg="green")

        # Username entry
        self.usernameentryLabel = Label(self.master, text="User Name", pady=10, padx=10).grid( row=0, column=0)
        self.user = StringVar()
        self.userEntry = Entry(self.master, textvariable=self.user).grid(row=0, column=1, pady=10, padx=10)


        # password entry
        self.passnameentryLabel = Label(self.master, text="Password", pady=11, padx=14).grid( row=1, column=0)
        self.password = StringVar()
        self.passwordEntry = Entry(self.master, textvariable=self.password, show="*").grid(row=1, column=1, pady=10, padx=10)

        # Button login
        self.login = Button(self.master, text= "Submit", command= self.loginvalidation, padx=10, pady=10).grid(row=3, column=5)
    def Newwindow(self):
        Home = Tk()
        myGui=dataentry(Home)









class dataentry:
    
    
    def __init__(self,master):
          
        self.model= {}
        self.master=master
    
        #function to add data to tree view
        def adddata():
            employees = Server.grabdata()
            self.tview.delete(*self.tview.get_children())
            for employee in employees:
                self.tview.insert('', END, values=employee)
                
        #function to delete data from tree view
        def delete1():
            selected = self.tview.focus()
            if not selected:
                messagebox.showerror('CRITICAL', 'Select Employee')
            else:
                id = identry.get()
                Server.deldata(id)
                adddata()
                messagebox.showinfo('success', 'data deleted')
                
        #update employee details
        def update1():
            employeeId = identry.get()
            employeename = nameentry.get()
            employeeExp = expentry.get()
            employeeAge = ageentry.get()
            employeePos = posentry.get()
            employeeRole = roleentry.get()
            employeePerf = perfentry.get()
            employeePay = payentry.get()
            employeeStrt = startentry.get()
            employeeEnd = endentry.get()
            Server.updatedata(employeeId, employeename,employeeExp, employeeAge, employeePos, employeeRole,employeePerf,employeePay,employeeStrt,employeeEnd)
            adddata()
            messagebox.showinfo('success', 'Data Updated')
            
            
                
        #add new employees       
        def addfunction():
            employeeId = identry.get()
            employeename = nameentry.get()
            employeeExp = expentry.get()
            employeeAge = ageentry.get()
            employeePos = posentry.get()
            employeeRole = roleentry.get()
            employeePerf = perfentry.get()
            employeePay = payentry.get()
            employeeStrt = startentry.get()
            employeeEnd = endentry.get()
            if not (employeeId and employeename and employeeExp and employeeAge and employeePos and employeeRole and employeePerf and employeePay and employeeStrt and employeeEnd):
                messagebox.showerror('CRITICAL', 'ENTER DATA INTO ALL FIELDS')
            elif Server.datacheck(employeeId):
                messagebox.showerror('CRITICAL', 'EMPLOYEE ALREADY EXISTS')
            else:
                Server.adddata(employeeId, employeename,employeeExp, employeeAge, employeePos, employeeRole,employeePerf,employeePay,employeeStrt,employeeEnd)
                adddata()
                messagebox.showinfo('success', 'employee added to database')
            
#all labels and buttons
        idlabel = Label(self.master, text="ID:")
        idlabel.place(x=30,y=30)
        identry = Entry(self.master)
        identry.place(x=110,y=30)
        
        namelabel = Label(self.master, text="Name:")
        namelabel.place(x=30,y=50)
        nameentry = Entry(self.master)
        nameentry.place(x=110,y=50)
        
        explabel = Label(self.master, text="Experience:")
        explabel.place(x=30,y=70)
        expentry = Entry(self.master)
        expentry.place(x=110,y=70)
        
        agelabel = Label(self.master, text="Age:")
        agelabel.place(x=30,y=90)
        ageentry = Entry(self.master)
        ageentry.place(x=110,y=90)
        
        poslabel = Label(self.master, text="Position:")
        poslabel.place(x=30,y=110)
        posentry = Entry(self.master)
        posentry.place(x=110,y=110)
        
        rolelabel = Label(self.master, text="Role:")
        rolelabel.place(x=30,y=130)
        roleentry = Entry(self.master)
        roleentry.place(x=110,y=130)
        
        perflabel = Label(self.master, text="Performance:")
        perflabel.place(x=30,y=150)
        perfentry = Entry(self.master)
        perfentry.place(x=110,y=150)
        
        paylabel = Label(self.master, text="Salary:")
        paylabel.place(x=30,y=170)
        payentry = Entry(self.master)
        payentry.place(x=110,y=170)
        
        startlabel = Label(self.master, text="Start Date:")
        startlabel.place(x=30,y=190)
        startentry = Entry(self.master)
        startentry.place(x=110,y=190)
        
        endlabel = Label(self.master, text="End Date:")
        endlabel.place(x=30,y=210)
        endentry = Entry(self.master)
        endentry.place(x=110,y=210)
        
        add = Button(self.master,command=addfunction, text="ADD EMPLOYEE", width=20)
        add.place(x=10,y=500)
        
        update = Button(self.master,text="UPDATE DETAILS", width=20, command=update1)
        update.place(x=150,y=500)
        
        delete = Button(self.master,text="DELETE", width=40, command=delete1)
        delete.place(x=10,y=520)
        
        
        #setting up tree view
        self.tview = ttk.Treeview(self.master,height=20)
        
        #assigning collumns
        self.tview['columns'] = ('employeeId', 'employeename','employeeExp', 'employeeAge', 'employeePos', 'employeeRole','employeePerf','employeePay','employeeStrt','employeeEnd')
        
        #collumn styles
        #hides original column
        self.tview.column('#0', width=0)
        self.tview.column('employeeId', width=100)
        self.tview.column('employeename', width=100)
        self.tview.column('employeeExp', width=100)
        self.tview.column('employeeAge', width=100)
        self.tview.column('employeePos', width=100)
        self.tview.column('employeeRole', width=100)
        self.tview.column('employeePerf', width=100)
        self.tview.column('employeePay', width=100)
        self.tview.column('employeeStrt', width=100)
        self.tview.column('employeeEnd', width=100)
        
        #headings for tree view columns
        self.tview.heading('employeeId', text= 'ID:')
        self.tview.heading('employeename', text= 'Name:')
        self.tview.heading('employeeExp', text= 'Experience:')
        self.tview.heading('employeeAge', text= 'Age:')
        self.tview.heading('employeePos', text= 'Position')
        self.tview.heading('employeeRole', text= 'Role:')
        self.tview.heading('employeePerf', text= 'Performance:')
        self.tview.heading('employeePay', text= 'pay')
        self.tview.heading('employeeStrt', text= 'Start Date:')
        self.tview.heading('employeeEnd', text= 'End Date:')
        
        
        
        #places tree view
        self.tview.place(x=350,y=30)
        #calls upon adddata function 
        adddata()
        
        
        










        
                

        #Main window declaration
        self.master=master
        self.master.title("Employee management")
        self.master.geometry("1440x720")
    
    
    
        

        


        










def main():
    tkMainWin = Tk()
    home = Main(tkMainWin)
    tkMainWin.mainloop()



if __name__=='__main__':
    main()
    
