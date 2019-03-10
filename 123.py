from tkinter import *
from tkinter import ttk
import sqlite3

class Product:
    def __init__(self,master):
        self.master=master
        self.master.title('Price')
        self.master.configure(background="cyan")

        frame=LabelFrame(self.master,text='Add new record',fg='black',bg='lightskyblue')
        frame.grid(row=0 ,column=1)
        
        Label(frame,text='Name:',bg='navyblue',fg='white').grid(row=1,column=1)
        self.name=Entry(frame)
        self.name.grid(row=1,column=2)
        


        Label(frame,text='Price:',bg='navyblue',fg='white').grid(row=2,column=1)
        self.price=Entry(frame)
        self.price.grid(row=2,column=2)

        ttk.Button(frame,text='Add Record',command=self.addding).grid(row=3,column=2)
        self.message=Label(text='',fg='red')
        self.message.grid(row=3,column=0)

        self.tree = ttk.Treeview(height=10,columns=(2,3))
        self.tree.grid(row=4,column=0,columnspan=3)
        
        self.tree.heading('#0',text='ID',anchor=W,)
        self.tree.heading('#1',text='Name',anchor=W)
        self.tree.heading('#2',text='Price',anchor=W)
        ttk.Style().configure("Treeview",background="navyblue",foreground="white")
        ttk.Button(text='Delete record' ,command=self.delete).grid(row=5,column=0)
        ttk.Button(text='Edit record',command=self.Edit).grid(row=5,column=1)
        

        self.viewing_re()
    

    def run_query(self,query,parameters=()):
        with sqlite3.connect('123.db') as conn:
            cursor=conn.cursor()
            query_result=cursor.execute(query,parameters)
            conn.commit
        return query_result


    def viewing_re(self):
        elements=self.tree.get_children()
        for i in elements:
            
            self.tree.delete(i)

        query='select*from product order by id desc'
        db_rows=self.run_query(query)
        for row in db_rows:
            self.tree.insert('',0,text=row[0],values=(row[1],row[2]))
        #ttk.Style().configure("Treeview",background="blue",fg="white")

    def validating(self):
        if len(self.name.get())!=0 and len(self.price.get())!=0:
            return True
    def addding(self):
        if self.validating()==True:
            query="insert into product values(NULL,?,?)"

            parameters=(self.name.get(),self.price.get())
            self.run_query(query,parameters)
            self.message['text']='Record Added'
            self.name.delete(0,END)
            self.price.delete(0,END)
        else:
            self.message['text']="Please fill again"
        self.viewing_re()

    def delete(self):
        
        wind=Toplevel(self.master)
        wind.title('Delete the data')
        f=ttk.Frame(wind)
        f.pack()
        f.config(height=500,width=1000)
        f.config(relief=RIDGE)
        self.iv=IntVar()
        Label(f,text='Id:',font=('Courier',15,'bold')).grid(row=1,column=1)
        self.id=ttk.Combobox(f, values = (1,2,3,4))
        self.id.grid(row=1,column=2)
        Label(f,text='Name:',font=('Courier',15,'bold')).grid(row=2,column=1)
        self.na=ttk.Entry(f)
        self.na.grid(row=2,column=2)
        Label(f,text='Price:',font=('Courier',15,'bold')).grid(row=3,column=1)
        self.pr=ttk.Entry(f)
        self.pr.grid(row=3,column=2)
        self.button=ttk.Button(f,text='Submit',command=self.de).grid(row=4,column=2)
        self.me=Label(f,text='',fg='Red')
        self.me.grid(row=5,column=1)
    
    def de(self):
        if len(self.pr.get())!=0 and len(self.pr.get())!=0 and int(self.id.get())>0:
            self.dele()

    def dele(self):
        query="delete from product where id =? or name=? or price=?"
        para=(int(self.id.get()),self.na.get(),self.pr.get())
        if self.run_query(query,para):
            self.na.delete(0,END)
            self.pr.delete(0,END)
            self.me['text']='Deleted Successfully !'

        
            
            
    def Edit(self):
        win=Toplevel(self.master)
        win.title('Delete the data')
        f1=ttk.Frame(win)
        f1.pack()
        f1.config(height=500,width=1000)
        f1.config(relief=RIDGE)
        
        Label(f1,text='Id:',font=('Courier',15,'bold')).grid(row=1,column=1)
        self.id1=ttk.Combobox(f1, values = (1,2,3,4))
        self.id1.grid(row=1,column=2)
        Label(f1,text='Name:',font=('Courier',15,'bold')).grid(row=2,column=1)
        self.na1=ttk.Entry(f1)
        self.na1.grid(row=2,column=2)
        Label(f1,text='Price:',font=('Courier',15,'bold')).grid(row=3,column=1)
        self.pr1=ttk.Entry(f1)
        self.pr1.grid(row=3,column=2)
        self.button1=ttk.Button(f1,text='Submit',command=self.ed).grid(row=4,column=2)
        self.me=Label(f1,text='',fg='Red')
        self.me.grid(row=5,column=1)
    

    def ed(self):
        query="update product set name=? ,price=? where id=?"
        para=(self.na1.get(),self.pr1.get(),int(self.id1.get()))
        if self.run_query(query,para):
            self.na1.delete(0,END)
            self.id1.delete(0,END)
            self.pr1.delete(0,END)
            self.me['text']='Edited Successfully'

        
        






        
if __name__=='__main__':
    
    root = Tk()
    application=Product(root)
    root.mainloop()
