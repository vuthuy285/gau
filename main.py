from flask import Flask,redirect, url_for, render_template, request, session, flash
from connectSQL import connectDB, checkExistAccount, getAllInfor, getInforUser, getPasswd

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
            user=getInforUser(name)
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
