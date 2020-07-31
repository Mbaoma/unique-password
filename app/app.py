from flask import Flask, jsonify, render_template, request
from pwned import check_pwned

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    password = request.form.get("password", None)
    if password:
        r = check_pwned(password)
        if r["success"]:
            result = "Your password has been breached {:,} times".format(r["count"])
        else:
            result = "An error occured while checking your password. Please try again later"
    return render_template("../templates/index.html", result=result)

@app.route("/check_pwned/<password>")
def pwned(password):
    r = check_pwned(password)
    return jsonify(r)

if __name__ == "__main__":
    app.run(debug=True)
