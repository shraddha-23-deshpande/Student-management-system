#-------------------------- Operations Performed

def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobval.get()
        email = emailval.get()
        add = addval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (id, name, mobile, email, add, gender, dob, addeddate, addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notificatrions','Id {} Name {} Added sucessfully.. and want to clean the form'.format(id,name),parent=addroot)
            if (res == True):
                idval.set('')
                nameval.set('')
                mobval.set('')
                emailval.set('')
                addval.set('')
                genderval.set('')
                dobval.set('')


        except:
            messagebox.showerror('Notifications','Id Already Exist try another id....',parent=addroot)
        strr = 'select* from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        #data clean
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)


    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='LightBlue')
    addroot.iconbitmap('student.ico')
    addroot.resizable(False,False)
    #_____________________________________________________________________________Add student labels
    idlabel = Label(addroot,text='Enter ID: ',bg='Silver',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot, text='Enter Name: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10, y=70)

    moblabel = Label(addroot, text='Enter Mobile: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12,anchor='w')
    moblabel.place(x=10, y=130)

    emaillabel = Label(addroot, text='Enter Email: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    Addresslabel = Label(addroot, text='Enter Address: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12,anchor='w')
    Addresslabel.place(x=10, y=250)

    gendlabel = Label(addroot, text='Enter Gender: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12,anchor='w')
    gendlabel.place(x=10, y=310)

    doblabel = Label(addroot, text='Enter D.O.B: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    doblabel.place(x=10, y=370)

    #--------------------------------------------------------------------------Add student entry

    idval = StringVar()
    nameval = StringVar()
    mobval=  StringVar()
    emailval = StringVar()
    addval = StringVar()
    genderval = StringVar()
    dobval = StringVar()


    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobentry = Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=mobval)
    mobentry.place(x=250, y=190)

    emailentry = Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=130)


    addentry = Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable =addval)
    addentry.place(x=250, y=250)

    genderentry = Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    ############################################################################ add button
    submitbtn = Button(addroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='Silver',activeforeground='white',bg='red',command=submitadd)
    submitbtn.place(x=150,y=420)

    addroot.mainloop()
def searchstudent():
        def search():
            id = idval.get()
            name = nameval.get()
            mobile = mobval.get()
            email = emailval.get()
            add = addval.get()
            gender = genderval.get()
            dob = dobval.get()
            addeddate = time.strftime("%d/%m/%Y")
            if(id != ''):
                strr = 'select *from studentdata1 where id =%s'
                mycursor.execute(strr,(id))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studenttable.insert('', END, values=vv)
            elif (name != ''):
                strr = 'select *from studentdata1 where id =%s'
                mycursor.execute(strr, (name))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studenttable.insert('', END, values=vv)
            elif (mobile != ''):
                strr = 'select *from studentdata1 where id =%s'
                mycursor.execute(strr, (mobile))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studenttable.insert('', END, values=vv)
            elif (email != ''):
                strr = 'select *from studentdata1 where id =%s'
                mycursor.execute(strr, (email))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studenttable.insert('', END, values=vv)

            elif (add != ''):
                strr = 'select *from studentdata1 where id =%s'
                mycursor.execute(strr, (add))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studenttable.insert('', END, values=vv)
            elif (gender != ''):
                strr = 'select *from studentdata1 where id =%s'
                mycursor.execute(strr, (gender))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studenttable.insert('', END, values=vv)
            elif (dob != ''):
                strr = 'select *from studentdata1 where id =%s'
                mycursor.execute(strr, (dob))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studenttable.insert('', END, values=vv)
            elif (addeddate != ''):
                strr = 'select *from studentdata1 where id =%s'
                mycursor.execute(strr, (addeddate))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studenttable.insert('', END, values=vv)

        searchroot = Toplevel(master=DataEntryFrame)
        searchroot .grab_set()
        searchroot.geometry('470x540+220+200')
        searchroot.title('Student Management System')
        searchroot.config(bg='LightBlue')
        searchroot.iconbitmap('student.ico')
        searchroot.resizable(False, False)
        # _____________________________________________________________________________search student labels
        idlabel = Label(searchroot, text='Enter ID: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
        idlabel.place(x=10, y=10)

        namelabel = Label(searchroot, text='Enter Name: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE,
                          borderwidth=3, width=12, anchor='w')
        namelabel.place(x=10, y=70)

        moblabel = Label(searchroot, text='Enter Mobile: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
        moblabel.place(x=10, y=130)

        emaillabel = Label(searchroot, text='Enter Email: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE,
                           borderwidth=3, width=12, anchor='w')
        emaillabel.place(x=10, y=190)

        Addresslabel = Label(searchroot, text='Enter Address: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE,
                             borderwidth=3, width=12, anchor='w')
        Addresslabel.place(x=10, y=250)

        gendlabel = Label(searchroot, text='Enter Gender: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE,
                          borderwidth=3, width=12, anchor='w')
        gendlabel.place(x=10, y=310)

        doblabel = Label(searchroot, text='Enter D.O.B: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
        doblabel.place(x=10, y=370)

        datelabel = Label(searchroot, text='Enter Date: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
        datelabel.place(x=10, y=430)

        # --------------------------------------------------------------------------Search student entry

        idval = StringVar()
        nameval = StringVar()
        mobval = StringVar()
        emailval = StringVar()
        addval = StringVar()
        genderval = StringVar()
        dobval = StringVar()
        dateval = StringVar()

        identry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
        identry.place(x=250, y=10)

        nameentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=nameval)
        nameentry.place(x=250, y=70)

        mobentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=mobval)
        mobentry.place(x=250, y=190)

        emailentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=emailval)
        emailentry.place(x=250, y=130)

        addentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=addval)
        addentry.place(x=250, y=250)

        genderentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=genderval)
        genderentry.place(x=250, y=310)

        dobentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=dobval)
        dobentry.place(x=250, y=370)

        dateentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=dateval)
        dateentry.place(x=250, y=430)

        ############################################################################ search button
        submitbtn = Button(searchroot, text='Search', font=('roman', 15, 'bold'), width=20, bd=5,
                           activebackground='Silver', activeforeground='white', bg='red', command=search)
        submitbtn.place(x=150, y=480)

        searchroot.mainloop()

def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata1 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted successfully...'.format(pp))
    strr = 'select *from studentdata1 '
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)


def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobval.get()
        email = emailval.get()
        address = addval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr, (name, mobile, email, address, gender, dob, date, time, id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified sucessfully...'.format(id), parent=updateroot)
        strr = 'select *from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+220+160')
    updateroot.title('Student Management System')
    updateroot.config(bg='LightBlue')
    updateroot.iconbitmap('student.ico')
    updateroot.resizable(False, False)
        # _____________________________________________________________________________update student labels
    idlabel = Label(updateroot, text='Enter ID: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text='Enter Name: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    moblabel = Label(updateroot, text='Enter Mobile: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    moblabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text='Enter Email: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    Addresslabel = Label(updateroot, text='Enter Address: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    Addresslabel.place(x=10, y=250)

    gendlabel = Label(updateroot, text='Enter Gender: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    gendlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text='Enter D.O.B: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text='Enter Date: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)

    timelabel = Label(updateroot, text='Enter Time: ', bg='Silver', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    timelabel.place(x=10, y=490)

    # --------------------------------------------------------------------------update student entry

    idval = StringVar()
    nameval = StringVar()
    mobval = StringVar()
    emailval = StringVar()
    addval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=mobval)
    mobentry.place(x=250, y=190)

    emailentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=130)

    addentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=addval)
    addentry.place(x=250, y=250)

    genderentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

    timeentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=timeval)
    timeentry.place(x=250, y=490)

        ############################################################################ update button
    submitbtn = Button(updateroot, text='Update', font=('roman', 15, 'bold'), width=20, bd=5,
                           activebackground='Silver', activeforeground='white', bg='red', command=update)
    submitbtn.place(x=150, y=540)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobval.set(pp[2])
        emailval.set(pp[3])
        addval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()
def showstudent():
    strr = 'select *from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)
def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),
        addeddate.append(pp[7]),addedtime.append(pp[8])
    dd = ['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
    df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)                  #csv----comma seperated value (file format)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications','Student data is saved {}'.format(paths))

def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you want to exit')
    if(res == True):
        root.destroy()

###################################################################################################### Connection of Database
def Connectdb():
    def submitdb():
        global con, mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications', 'Data is incorrect please try again', parent=dbroot)
            return
        try:
            strr = 'create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'create table studentdata1(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification',
                                'database created and now you are connected connected to the database ....',
                                parent=dbroot)

        except:
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Now you are connected to the database ....', parent=dbroot)
        dbroot.destroy()
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('student.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='CadetBlue')
    #-------------------------Connectdb Labels
    hostlabel = Label(dbroot,text="Enter host : ",bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot, text="Enter user : ", bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=13, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text="Enter password : ", bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=13, anchor='w')
    passwordlabel.place(x=10, y=130)

    #-----------------------------------------------------------------------------------Connectdb Entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)

    #-------------------------------------------------------------------------connectdb button
    submitbutton = Button(dbroot,text='Submit',font=('roman',15,'bold'),width=20,bg='red',bd=5,activebackground='CadetBlue',
                          activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()

###############################################################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%y")
    clock.config(text='Date:'+date_string+"\n"+"Time: "+time_string)
    clock.after(200,tick)
################################################################# IntroSlider


def IntroLabelTick():
    global count,text
    if(count >= len(ss)):
        count = -1
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
    count +=1
    SliderLabel.after(150,IntroLabelTick)

########################################################################## import function
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
import time
import pymysql
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import pandas


root = Tk()
root.title('Student Management System')
root.config(bg='grey')
root.geometry('1174x700+200+50')
root.iconbitmap('student.ico')
root.resizable(False, False)
############################################################################################ Frames

################################################################################################################################# dataentry Frame
DataEntryFrame = Frame(root,bg='grey',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)

frontlabel = Label(DataEntryFrame,text='---------------Welcome---------------',width=25,font=('arial',22,'italic bold'),bg='grey')
frontlabel.pack(side=TOP,expand=True)

addbtn = Button(DataEntryFrame,text='1.Add Student',width=25,font=('chiller',20,'bold'),bd=6,bg='FloralWhite',activebackground='CadetBlue',relief=RIDGE,
                activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2.Search Student',width=25,font=('chiller',20,'bold'),bd=6,bg='FloralWhite',activebackground='CadetBlue',relief=RIDGE,
                   activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3.Delete Student',width=25,font=('chiller',20,'bold'),bd=6,bg='FloralWhite',activebackground='CadetBlue',relief=RIDGE,
                   activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4.Update Student',width=25,font=('chiller',20,'bold'),bd=6,bg='FloralWhite',activebackground='CadetBlue',relief=RIDGE,
                   activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showbtn = Button(DataEntryFrame,text='5.Show All',width=25,font=('chiller',20,'bold'),bd=6,bg='FloralWhite',activebackground='CadetBlue',relief=RIDGE,
                 activeforeground='white',command=showstudent)
showbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='6.Export Data',width=25,font=('chiller',20,'bold'),bd=6,bg='FloralWhite',activebackground='CadetBlue',relief=RIDGE,
                   activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7.Exit',width=25,font=('chiller',20,'bold'),bd=6,bg='Linen',activebackground='CadetBlue',relief=RIDGE,
                 activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)


########################################################################################################### Show data frame
ShowDataFrame = Frame(root,bg='grey',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)
style = ttk.Style()
style.configure('Treeview.Heading',font=('times',20,'bold'),foreground='black')
style.configure('Treeview.Heading',font=('times',20,'bold'),foreground='black',background='AliceBlue')
#-----------------------------------------------------------------------show data frame
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)

studenttable = Treeview(ShowDataFrame,columns=('ID','Name','Mob','Email','Address','Gender','DOB','Added Date','Added Time'),
                        yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)

studenttable.heading('ID',text='ID')
studenttable.heading('Name',text='Name')
studenttable.heading('Email',text='Email')
studenttable.heading('Mob',text='Mob')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('DOB',text='DOB')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show'] = 'headings'
studenttable.column('ID',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mob',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('DOB',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)
studenttable.pack(fill=BOTH,expand=1)

###################################################################################################### Slider
ss = 'Welcome To Student Management System'
count = 0
text = ''
#########################################
SliderLabel = Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=4,width=25,bg='white')
SliderLabel.place(x=260,y=0)
IntroLabelTick()

############################################################################################################ Time
clock = Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='white')
clock.place(x=0,y=0)
tick()
########################################################################################## ConnectDatabaseButton
connectbutton =Button(root,text='Connect To Dataset',width=23,font=('chiller',14,'italic bold'),relief=RIDGE,borderwidth=4,bd=6,bg='white',
                      activebackground='CadetBlue',activeforeground='white',command=Connectdb)
connectbutton.place(x=930,y=0)
root.mainloop()

