import pyodbc
from flask import Flask,redirect, url_for, render_template, request, session, flash
# from connectSQL import connectDB, checkExistAccount, getAllInfor, getInforUser, getPasswd

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
    cursor.execute("SELECT username FROM nhan_vien WHERE username= '" +user_name+ "' and pass= '" +passwd+ "'")
    for row in cursor:
        return row    
    

def getAllInfor():
    users=[]
    conn=connectDB()
    cursor=conn.cursor()
    cursor.execute("""
    SELECT ID, USERNAME, HOTEN, PASS, EMAIL, SDT, TENPB, TENCV, CHUYENNGANH, LUONGCB*HSL AS LUONG
    FROM (NHAN_VIEN JOIN LUONG ON NHAN_VIEN.BacLuong=LUONG.BacLuong) JOIN PHONG_BAN ON NHAN_VIEN.MaPB=PHONG_BAN.MaPB 
																	JOIN CHUC_VU ON NHAN_VIEN.MaCV=CHUC_VU.MaCV
																	JOIN TRINH_DO_HOC_VAN ON TRINH_DO_HOC_VAN.MaTDHV=NHAN_VIEN.MaTDHV
    """)
    for row in cursor.fetchall():
        users.append({"ID": row[0], "username": row[1], "name": row[2], "pass": row[3], "email": row[4], "phone": row[5], "phong": row[6], "chucvu": row[7], "chuyennganh": row[8], "luong": int(row[9])})
    return users

def getOneUser(user_name):
    conn=connectDB()
    cursor=conn.cursor()
    # cursor.execute("SELECT username FROM thong_tin WHERE username=? and pass=?", user_name, passwd)
    cursor.execute("""
    SELECT ID, USERNAME, PASS, HOTEN, EMAIL, SDT, TENPB, TENCV, CHUYENNGANH, LUONGCB*HSL AS LUONG
    FROM (NHAN_VIEN JOIN LUONG ON NHAN_VIEN.BacLuong=LUONG.BacLuong) JOIN PHONG_BAN ON NHAN_VIEN.MaPB=PHONG_BAN.MaPB 
																	JOIN CHUC_VU ON NHAN_VIEN.MaCV=CHUC_VU.MaCV
																	JOIN TRINH_DO_HOC_VAN ON TRINH_DO_HOC_VAN.MaTDHV=NHAN_VIEN.MaTDHV
    WHERE USERNAME= '""" +user_name+ """ '""")
    user = cursor.fetchone()
    return user
    
# def getPasswd(user_name):
#     conn=connectDB()
#     cursor=conn.cursor()
#     # cursor.execute("SELECT username FROM thong_tin WHERE username=? and pass=?", user_name, passwd)
#     cursor.execute("SELECT pass FROM thong_tin WHERE username= '" +user_name+  "'")
#     for p in cursor:
#         return p


app = Flask(__name__)
app.config["SECRET_KEY"] = "thuy1234" #ma hoa session cookie de tranh bi tan cong

@app.route("/")
@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method=="POST":
        user_name=request.form["name"]
        passwd=request.form["password"]
        row=checkExistAccount(user_name, passwd)
        if row:
            createSession(user_name)
            return redirect(url_for("welcomeUser", name=user_name))
    if "user" in session:
        user_name=session["user"]
        return redirect(url_for("welcomeUser", name=user_name))
    return render_template('login.html')

def createSession(user_name):
    session["user"] = user_name

@app.route("/user")
def welcomeUser():
    if "user" in session:
        name=session["user"]
        if name=="admin":
            return render_template('admin.html', name=name)    
        else:
            return render_template('user.html', name=name)
    return render_template('login.html')


@app.route("/logout", methods=['GET', 'POST'])
def logout(): 
    if request.method=="POST":
        session.pop("user", None)
        return redirect(url_for("login"))

@app.route("/return", methods=['GET', 'POST'])
def rerturn(): 
    if request.method=="POST":
        if "user" in session:
            name=session["user"]
            return redirect(url_for("welcomeUser", name=name))    

@app.route("/select")
def selectInfo():
    if "user" in session:
        name=session["user"]
        if name == "admin":
            users=getAllInfor()
            return render_template("userlist.html", users=users, name=name)
        else:
            user=getOneUser(name)
            print(user)
            return render_template("userlist.html", user=user, name=name)
    return render_template('login.html')

# @app.route("/find")
# def findInfo(user_name):
#     if "user" in session:
#         x=getPasswd(user_name)

@app.route("/delete")
def delete():
    return f"<h2>Delete Complete!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
