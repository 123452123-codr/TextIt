import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="admin", database="textit")
cur = con.cursor()

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel  
from pyqt5.QtGui import QFont
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CHATTING APP MADE BY GEEKS")
        self.setGeometry(0,0,1000,1000) 
        label=Qlabel("Username:")
        label.setfont(QFont("Calibri",45))
        label.setGeometry(0,0,500,100)
                                    

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()


def signUp():

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

def forgotPassword(user):
    cur.execute("select username from users where username=%s", (user,))
    result1 = cur.fetchall()

    if result1:
        ph = int(input("Enter the phone number:"))
        cur.execute("select phone from users where username=%s and phone=%s", (user,ph))
        result2 = cur.fetchall()

        if result2:
            new_password = input("Enter new password:")
            cur.execute("update users set password=%s where username=%s",(new_password,user))
            con.commit()
            print("password updated successfully")
        else:
            print("Phone number doesn't match")
    else:
        print("User doesn't exist")
    #for this function, ask the user first for username, check via the function and proceed for phone number only if the username exists, as programmed in the function. then ask for phone number and validate. replace the inputs and texts with appropriate labels and text boxes.

def signIn(username, password):
    cur.execute("select password from users where username=%s and password=%s",(username, password))
    x = cur.fetchall()
    if x:
        global self_username
        self_username = username
        pass
        #insert appropriate GUI functions for moving on to chat screen.

def createChat(username):
    cur.execute("select username from users where username=%s",(username,))
    r = cur.fetchall()
    if r:
        global members, t_name
        t_name = self_username+"_"+username
        members = (self_username, username)
        cur.execute("create table %s(Sender not null, Receiver not null, Message not null)",(t_name,))
        message = ""
        con.commit()

def chatting(message):
    if message != "":
        cur.execute("insert into %s values(%s, %s, %s)",(t_name, members[0], members[1], message))
        print("message inserted successfully")







