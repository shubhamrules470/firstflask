from flask import Flask,render_template,request,url_for,redirect
import sqlite3 as sq
import sqlite3 as s
con = s.connect('sarthak_ka_database.db')
with con:
    cur=con.cursor()
    cur.execute("Create table if not exists details(fname text not null,lname text,email text primary key not null,password text not null,weight int not null,height int not null,profession text,gender text)")


username=None

app=Flask(__name__)
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/login",methods =['GET','POST'])
def login():
	error =None
	if request.method == 'POST':
		username = request.form['email']
		password = request.form['password']
		con = sq.connect('sarthak_ka_database.db')
		with con:
			cur=con.cursor()
			try:
				cur.execute("""SELECT fname,password  from details where email = ? """,(username,))
				d=cur.fetchone()
				#print(d)
				fn = d[0]
				pas = d[1]
				if password == pas :
					username = fn
					print(username)
					return redirect(url_for('chatbot'))
				else:
					error = "Invaild Email or Password"

			except :
				print('Unsuccessful')
		#print(username,password)
	return render_template('login2.html',error=error)


@app.route("/signup", methods =['GET','POST'])
def signup():
	if request.method == 'POST':
		fname = request.form['first_name']
		lname = request.form['last_name']
		bday = request.form['bday']
		email = request.form['email']
		ps= request.form['password']
		weight = request.form['weight']
		height = request.form['height']
		prof = request.form['profession']
		gen = request.form['gender']
		con = sq.connect('sarthak_ka_database.db')
		with con:
			cur = con.cursor()
			
			cur.execute("""INSERT INTO details(fname,lname,email,password,weight,height,profession,gender)VALUES(?,?,?,?,?,?,?,?)""",(fname,lname,email,ps,weight,height,prof,gen))

		return redirect(url_for('login'))




		print(fname,lname,bday,email,ps,weight,height,prof,gen)
	return render_template('Signup.html')

@app.route("/chatbot")
def chatbot():
	usr = username
	print(username)
	return render_template('chat.html',username = usr)
	print(usr)

if __name__=="__main__":
	app.run(port=5000,debug=True)
