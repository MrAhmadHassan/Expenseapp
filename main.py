from flask import Flask,render_template,request,redirect
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(host='localhost',user="root",password="",database="expenseapp")
cursor = conn.cursor()
@app.route('/')
def login():
    return render_template('./login.html')

@app.route('/signup')
def register():
    return render_template('./signup.html')

@app.route('/home')
def home():
    return render_template('./home.html')

@app.route('/login_validator',methods=['POST'])
def login_validator():
    email = request.form.get('email')
    password = request.form.get('password')
    print(email)
    print(password)

    cursor.execute("""SELECT * FROM `employes` WHERE email LIKE '{}' AND password LIKE '{}' """.format(email,password))
    users=cursor.fetchall()
    if len(users)>0:
        return redirect('/home')
    else:
        return redirect('/login')


@app.route('/signup_validator',methods=['POST'])
def signup_validator():
    name=request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    cursor.execute("""INSERT INTO employes (name,email,password) VALUE ('{}','{}','{}')""".format(name,email,password))
    conn.commit()
    return "Registration successful"





if __name__ == "__main__":
    app.run(debug=True)
