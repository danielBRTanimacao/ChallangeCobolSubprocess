from flask import Flask

app = Flask(__name__)

@app.route("/api/withdraw", methods=["GET"])
def withdraw_value():
    return "1"

@app.route("/api/deposit", methods=["POST"])
def deposit_value():
    return "1"

if __name__ == "__main__":
    app.run(debug=True)