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
    