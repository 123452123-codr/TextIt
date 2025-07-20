import mysql.connector
from cryptography.fernet import Fernet
import datetime

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root", 
        password="admin", 
        database="textit", 
        charset="utf8"
    )
    if con.is_connected():
        cur = con.cursor()
        
except mysql.connector.Error as err:
    print("Error connecting to server:",err)

key = Fernet.generate_key()
f = Fernet(key)

def signUp(username,name,phone,password):
    status = "Account created"
    encoded_password = str(password).encode()
    encrypted_password = f.encrypt(encoded_password)
    comm = "insert into users (username,name,phone,password,status) values(%s,%s,%s,%s,%s)"
    val = (username,name,phone,encrypted_password,status)
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
            encoded_password = new_password.encode()
            new_encrypted_password = f.encrypt(encoded_password)
            cur.execute("update users set password=%s where username=%s",(new_encrypted_password,user))
            con.commit()
        else:
            return ("Phone number doesn't match")
    else:
        return ("User doesn't exist")
    #for this function, ask the user first for username, check via the function and proceed for phone number only if the username exists, as programmed in the function. then ask for phone number and validate. replace the inputs and texts with appropriate labels and text boxes.

def signIn(username, password):
    encoded_password = str(password).encode()
    enc_pass = f.encrypt(encoded_password)
    cur.execute("select password from users where username=%s and password=%s",(username, enc_pass))
    x = cur.fetchall()
    if x:
        global self_username
        self_username = username
        cur.execute("update users set status=%s where username=%s",("Signed In",self_username))
        con.commit()
        #insert appropriate GUI functions for moving on to chat screen.
    else:
        return ("User not found.")

def createChat(username):
    cur.execute("select username from users where username=%s",(username,))
    r = cur.fetchall()
    if r:
        global members, table_name
        table_name = self_username+"_"+username
        members = (self_username, username)
        cur.execute("create table %s(ID int auto_increment primary key, Sender not null, Receiver not null, Message not null, Date_of_message date not null,Time_of_message time not null)",(table_name,))
        message = ""
        con.commit()
        return message

def sendMessage(message):
    if message != " ":
        x = datetime.datetime.now()
        date = x.date()
        time = x.time()
        cur.execute("insert into %s(sender,receiver,message,date_of_message,time_of_message) values(%s, %s, %s, %s, %s)",(table_name, members[0], members[1], message, date, time))
        con.commit()
    else:
        pass

def receiveMessage():
    cur.execute("select * from %s where id=(select last_insert_id())")
    message = cur.fetchall()
    s,r,m,d,t = message
    return s,r,m,d,t

def removeChat(chatname):
    cur.execute("drop table %s",(chatname,))
    con.commit()
    return ("Chat deleted successfully.")

def signOut():
    cur.execute("update users set status=%s where username=%s",("Signed Out", self_username))
    con.commit()
    return ("Logged out")

def deleteAccount():
    cur.execute("show tables from textit where Tables_in_textit like '%{}%'".format(self_username))
    tables = cur.fetchall()
    for i in tables:
        removeChat(i)

    cur.execute("delete from users where username=%s",(self_username,))
    con.commit()

    return ("Account deleted successfully")
