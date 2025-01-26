import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Arpit@123"
    # database="Library Management System"
    )
mycursor=mydb.cursor()

print("""-------------------------------------
Welcome To Library Management System
-------------------------------------""")

#Creating Database
mycursor.execute("CREATE DATABASE IF NOT EXISTS Library_Management")
mycursor.execute("USE Library_Management")
mycursor.execute("CREATE TABLE IF NOT EXISTS availabale_Books(id int,name varchar(25),subject varchar(25),quantity int)")
mycursor.execute("CREATE TABLE IF NOT EXISTS issued(id int,name varchar(25),subject varchar(25),s_name varchar(25),s_class varchar(25))")
mycursor.execute("CREATE TABLE IF NOT EXISTS login(user varchar(25),password varchar(25))")
mydb.commit() 
flag=0
mycursor.execute("SELECT * FROM login")
for i in mycursor:
    flag=1
if flag==0:
    mycursor.execute("INSERT into login values('user','arpit')")
    mydb.commit()
#####################################\\Main working

while True:
    print("""1.Login
2.EXit
""")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        pas=input("Enter Your Password:")
        mycursor.execute("SELECT * FROM login")
        for i in mycursor:
            t_user,t_pass=i
        if pas==t_pass:
            print("Login Successfully...") 
            loop1='n'
            while loop1=='n':
                print("""----------------------------
1.Add New Book
2.Remove Any Boook
3.Issue Book To Student
4.Return Book
5.View Available Books
6.View Issued Books
7.Logout
-----------------------------
    """)
                ch=int(input("Enter Your Choice:"))
                if ch==1:
                    loop2='y'
                    while loop2=='y':
                        print("All Information are maindatory to be filled!!!")
                        idd=int(input("Enter Book ID:"))
                        name=input("Enter Book Name:")
                        subject=input("Enter Subject:")
                        quan=int(input("Enter Quantity:"))
                        mycursor.execute("INSERT INTO availabale_Books VALUES('"+str(idd)+"','"+name+"','"+subject+"','"+str(quan)+"')")
                        mydb.commit()
                        print("Data Inseerted Successfully.....")
                        loop2=input("Do You Want TO Add Another Book?(y/n)").lower()
                    loop1=input("Do You Want TO Logout?(y/n)").lower()
                elif ch==2:
                    idd=int(input("Enter ID to Remove Book:"))
                    mycursor.execute("SELECT * FROM availabale_Books")
                    flag=0
                    for i in mycursor:
                        t_id,t_name,t_subject,t_quan=i
                        if t_id==idd:
                            flag=1
                    if flag==1:
                        mycursor.execute("DELETE FROM availabale_Books WHERE id='"+str(idd)+"'")
                        mydb.commit()
                        print("Data Successfuly Deleted....")
                    else:
                        print("Wrong ID....")
                elif ch==3:
                    loop2='y'
                    while loop2=='y':
                        idd=int(input("Enter Book ID:"))
                        s_name=input("Enter Student Name:")
                        s_class=input("Enter Student Class:")
                        mycursor.execute("SELECT * FROM availabale_Books WHERE id='"+str(idd)+"'")
                        flag=0
                        for i in mycursor:
                            t_id,t_name,t_subject,t_quan=i
                            flag=1
                        quan=t_quan-1
                        if flag==1:
                            if t_quan>=0:
                                mycursor.execute("INSERT INTO issued VALUES('"+str(idd)+"','"+t_name+"','"+t_subject+"','"+s_name+"','"+s_class+"')")
                                mycursor.execute("UPDATE availabale_Books SET quantity='"+str(quan)+"' where id='"+str(idd)+"'")
                                mydb.commit()
                                print("Successfully Issued....")
                                loop2=input("Do You Want To Issue more Books?(y/n)").lower()
                            else:
                                print("Book Not available....")
                        else:
                            print("Invalid Input....")
                    loop1=input("Do You Want to Logout?(y/n)").lower()
                    
                elif ch==4:
                    loop2='y'
                    while loop2=='y':
                        idd=int(input("Enter Book ID:"))
                        s_name=input("Enter Student Name:")
                        s_class=input("Enter Student Class:")
                        mycursor.execute("SELECT * FROM issued")
                        flag=0
                        for i in mycursor:
                            t_id,t_name,t_subject,t_s_name,t_s_class=i
                            if t_id==idd and t_s_name==s_name and t_s_class==s_class:
                                flag=1
                        if flag==1:
                            mycursor.execute("SELECT * FROM availabale_Books WHERE id='"+str(idd)+"'")
                            for i in mycursor:
                                t_id,t_name,t_subject,t_quan=i
                                quan=t_quan+1
                                mycursor.execute("DELETE FROM issued WHERE id='"+str(idd)+"'and s_name='"+s_name+"'and s_class='"+s_class+"'")
                                mycursor.execute("UPDATE availabale_Books set quantity='"+str(quan)+"'")
                                mydb.commit()
                                print("Successfully Issued...")
                                loop2=input("Do You Want to issue more Books?(y/n)").lower()
                        else:
                            print("Not Issued yet...")
                    loop1=input("Do You Want to Logout?(y/n)").lower()
                elif ch==5:
                    mycursor.execute("SELECT * FROM availabale_Books")
                    print("ID | Name | Subject | Quantity")
                    for i in mycursor:
                        a,b,c,d=i
                        print(f"{a} | {b} | {c} | {d}")
                elif ch==6:
                    mycursor.execute("SELECT * FROM issued")
                    print("ID | Name | Subject | S_Name | S_Class")
                    for i in mycursor:
                        a,b,c,d,e=i
                        print(f"{a}| {b} | {c} | {d} |{e}")
                elif ch==7:
                    break

        else:
            print("Wrong Password....")

    elif ch==2:
        break