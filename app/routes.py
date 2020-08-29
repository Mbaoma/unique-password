from flask import *
from script import check_password

#define the routes
app = Flask(__name__,
        template_folder = '../templates',
        static_folder = '../static')
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/confirmation")
def confirmation():
	return render_template('confirmation.html')

@app.route("/check/<password>") 
def check(password):
	result = None 
	password = request.form.get("password", None)
	r = check_password(password) 

@app.route('/check', methods=["GET", "POST"])
def checkin():
	result = None 
	password = request.form.get("password", None)
	r = check_password(password)
	if password: 
		if r["success"] == True and r["count"] == 0:
			result = 'Your password has been breached {: } times'.format(r['count'])
			return render_template('confirmation.html', result=result)
		else:
			result = 'Your password has been breached {: } times'.format(r['count'])
			return render_template('confirmation.html', result=result)
	return render_template('home.html', result=result)

if __name__ == "__main__":
    app.run()
