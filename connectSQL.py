import pyodbc

def connectDB():
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-0PSVL5P\MSQLSERVER1;"
        "Database=QLNV;"
        "Trusted_Connection=yes;"
    )
    return conn

def checkExistAccount(user_name, passwd):
    print(1)
    user=[]
    conn=connectDB()
    cursor=conn.cursor()
    # cursor.execute("SELECT username FROM thong_tin WHERE username=? and pass=?", user_name, passwd)
    cursor.execute("SELECT username FROM thong_tin WHERE username= '" +user_name+ "' and pass= '" +passwd+ "'")
    for row in cursor:
        return row    
    

def getAllInfor():
    users=[]
    conn=connectDB()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM thong_tin")
    for row in cursor.fetchall():
        users.append({"ID": row[0], "username": row[1], "name": row[2], "pass": row[3]})
    return users

def getInforUser(user_name):
    conn=connectDB()
    cursor=conn.cursor()
    # cursor.execute("SELECT username FROM thong_tin WHERE username=? and pass=?", user_name, passwd)
    cursor.execute("SELECT * FROM thong_tin WHERE username= '" +user_name+  "'")
    user = cursor.fetchone()
    return user
    
def getPasswd(user_name):
    conn=connectDB()
    cursor=conn.cursor()
    # cursor.execute("SELECT username FROM thong_tin WHERE username=? and pass=?", user_name, passwd)
    cursor.execute("SELECT pass FROM thong_tin WHERE username= '" +user_name+  "'")
    for p in cursor:
        return p