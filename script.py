import PyQt5 as p
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="admin", database="textit")
cur = con.cursor()

def add_user():

    username = input("Enter the username:")
    name = input("Enter the name:")
    phone = int(input("Enter phone number:"))
    password = input("Enter password:")
    #later, convert the above to GUI with pyqt5

    comm = "insert into users (username,name,phone,password) values(%s,%s,%s,%s)"
    val = (username,name,phone,password)
    cur.execute(comm,val)

    con.commit()
    #give necessary feedback in GUI (loading icon and then navigation to the next page)

def forgot_password(user):
    t = (user,)
    cur.execute("select username from users where username=%s", t)
    result = cur.fetchall()

    if result:
        ph_check = int(input("Enter your phone number to validate:"))
        cur.execute("select phone from users where username=%s", t)
        ph_tuple = cur.fetchall()
        ph = ph_tuple[0]
        #error over here... unable to compare ph and ph_check in line 33
        if ph == ph_check:

            new_password = input("Enter new password:")
            cur.execute("update users set password=%s where username=%s",(new_password,user))
            con.commit()
            print("password updated successfully")
        else:
            print("Phone number doesn't match")
    else:
        print("User doesn't exist")

u = input("Enter username to change the password:")
forgot_password(u)

