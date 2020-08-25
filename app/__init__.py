from flask import Flask, jsonify, render_template, request
from main import pwned_api_validator

app = Flask(__name__,
        template_folder = '../templates',
        static_folder = '../static')

@app.route("/")
def home():
    return render_template(url_for('index.html'))

@app.route("/passwordcheck", methods=["GET", "POST"])
def passwordcheck():
    result = None
    password = request.form.get("password", None)
    if password:
        r = pwned_api_validator(password)
        if r["success"]:
            result = "Your password has been breached {:,} times".format(r["count"])
        else:
            result = "An error occured while checking your password. Please try again later"
    return render_template(url_for('index'), result=result)
'''
@app.route("/check_pwned/<password>")
def pwned(password):
    r = check_pwned(password)
    return jsonify(r)
'''

if __name__ == "__main__":
    app.run()
