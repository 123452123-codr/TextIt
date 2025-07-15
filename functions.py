import mysql.connector
from cryptography.fernet import Fernet
import datetime

con = mysql.connector.connect(host="localhost", user="root", password="admin", database="textit")
cur = con.cursor()

key = Fernet.generate_key()
f = Fernet(key)

def signUp(username,name,phone,password):
    #later, convert the above to GUI with pyqt5 
    status = "Account created"
    comm = "insert into users (username,name,phone,password,status) values(%s,%s,%s,%s,%s)"
    val = (username,name,phone,password,status)
    cur.execute(comm,val)

    con.commit()
    return True
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
        cur.execute("update users set status=%s where username=%s",("Signed In",self_username))
        con.commit()
        #insert appropriate GUI functions for moving on to chat screen.
    else:
        print("User not found.")

def createChat(username):
    cur.execute("select username from users where username=%s",(username,))
    r = cur.fetchall()
    if r:
        global members, table_name
        table_name = self_username+"_&_"+username
        members = (self_username, username)
        cur.execute("create table %s(ID int auto_increment primary key, Sender not null, Receiver not null, Message not null, Date_of_message date,Time_of_message time)",(table_name,))
        message = ""
        con.commit()

def sendMessage(message):
    if message != " ":
        encrypted_message = f.encrypt(message)
        x = datetime.datetime.now()
        date = x.date()
        time = x.time()
        cur.execute("insert into %s(sender,receiver,message,date_of_message,time_of_message) values(%s, %s, %s, %s, %s)",(table_name, members[0], members[1], encrypted_message, date, time))
        print("message inserted successfully")
        con.commit()
    else:
        pass

def receiveMessage():
    cur.execute("select * from %s where id=(select last_insert_id())")
    message_data = cur.fetchall()


    return message_data

def removeChat(chatname):
    cur.execute("drop table %s",(chatname,))
    con.commit()
    print("Chat deleted successfully.")

